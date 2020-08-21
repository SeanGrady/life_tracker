from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Float,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import (
    declarative_base,
    declared_attr,
)
from sqlalchemy.orm import (
    relationship,
)
from flask_login import UserMixin as FlaskLoginMixin
from .security import (
    pwd_context,
)


Base = declarative_base()


class AppUserMixin(object):
    @declared_attr
    def app_user_id(cls):
        return Column(
            Integer,
            ForeignKey('app_user.id'),
            nullable=False,
            primary_key=True,
        )


class AppUser(FlaskLoginMixin, Base):
    __tablename__ = 'app_user'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )

    password_hash = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(
        String,
        unique=True,
    )

    mood_survey_responses = relationship(
        'MoodSurveyResponse',
        backref='app_user',
    )
    sleep_survey_responses = relationship(
        'SleepSurveyResponse',
        backref='app_user',
    )
    weigh_ins = relationship(
        'WeighIn',
        backref='app_user',
    )
    loseit_foods = relationship(
        'LoseitFood',
        backref='app_user',
    )

    def set_password(self, password):
        hashed = self.encrypt_password(password)
        self.password_hash = hashed

    def check_password(self, password):
        return self.check_encrypted_password(password, self.password_hash)

    def encrypt_password(self, password):
        return pwd_context.encrypt(password)

    def check_encrypted_password(self, password, hashed):
        return pwd_context.verify(password, hashed)


class LoseitFood(Base, AppUserMixin):
    __tablename__ = 'loseit_food'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    raw_date = Column(Date)
    raw_name = Column(String)
    raw_type = Column(String)
    raw_quantity = Column(Float)
    raw_units = Column(String)
    raw_calories = Column(Integer)
    raw_fat_g = Column(Float)
    raw_protein_g = Column(Float)
    raw_carbohydrates_g = Column(Float)
    raw_saturated_fat_g = Column(Float)
    raw_sugars_g = Column(Float)
    raw_fiber_g = Column(Float)
    raw_cholesterol_mg = Column(Float)
    raw_sodium_mg = Column(Float)


class DailyLogMixin(object):
    @declared_attr
    def date(cls):
        return Column(
            Date,
            primary_key=True,
            nullable=False,
        )


class BodyFatPercentage(Base, AppUserMixin, DailyLogMixin):
    __tablename__ = 'body_fat_percentage'
    body_fat_percentage = Column(Float)


class WeighIn(Base, AppUserMixin, DailyLogMixin):
    __tablename__ = 'weigh_in'
    weight_lbs = Column(Float)


class GformResponseMixin(object):
    @declared_attr
    def date_time(cls):
        return Column(
            DateTime,
            nullable=False,
            primary_key=True,
        )


class SleepSurveyResponse(Base, AppUserMixin, GformResponseMixin):
    __tablename__ = 'sleep_survey_response'
    sleep_quality = Column(Integer)
    sleep_hours = Column(Float)
    rise_ease = Column(Integer)


class MoodSurveyResponse(Base, AppUserMixin, GformResponseMixin):
    __tablename__ = 'mood_survey_response'
    mood = Column(Integer)
    energy = Column(Integer)
    adderall_crash = Column(Integer)
    sleep_hours = Column(Float)


class CronometerExportMixin(object):
    @declared_attr
    def date_time(cls):
        return Column(
            DateTime,
            nullable=False,
            primary_key=True,
        )


class CronometerExercise(Base, AppUserMixin, CronometerExportMixin):
    __tablename__ = 'cronometer_exercise'
    exercise = Column(
        String,
        nullable=False,
        primary_key=True,
    )
    group = Column(String)
    mintues = Column(Float)
    calories_burned = Column(Float)


