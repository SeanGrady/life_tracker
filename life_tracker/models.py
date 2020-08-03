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


class AppUser(Base):
    __tablename__ = 'app_user'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
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
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)


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
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    date = Column(
        Date,
        primary_key=True,
        nullabel=False,
    )


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


class BodyFatPercentage(Base, AppUserMixin, DailyLogMixin):
    __tablename__ = 'body_fat_percentage'
    body_fat_percentage = Column(Float)
