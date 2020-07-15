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
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class LoseitFood(Base):
    __tablename__ = 'loseit_food'
    id = Column(Integer, primary_key=True)
    app_user_id = Column(
        Integer,
        ForeignKey('app_user.id'),
        nullable=False,
    )
    app_user = relationship(
        'AppUser',
        back_populates='loseit_foods',
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


class WeighIn(Base):
    __tablename__ = 'weigh_in'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    weight_lbs = Column(Float)
    app_user_id = Column(
        Integer,
        ForeignKey('app_user.id'),
        nullable=False,
    )
    app_user = relationship(
        'AppUser',
        back_populates='weigh_ins',
    )


class SleepSurveyResponse(Base):
    __tablename__ = 'sleep_survey_response'
    app_user_id = Column(
        Integer,
        ForeignKey('app_user.id'),
        nullable=False,
        primary_key=True,
    )
    app_user = relationship(
        'AppUser',
        back_populates='sleep_survey_responses',
    )
    date_time = Column(
        DateTime,
        primary_key=True,
    )
    sleep_quality = Column(Integer)
    sleep_hours = Column(Float)
    rise_ease = Column(Integer)



class MoodSurveyResponse(Base):
    __tablename__ = 'mood_survey_response'
    app_user_id = Column(
        Integer,
        ForeignKey('app_user.id'),
        nullable=False,
        primary_key=True,
    )
    app_user = relationship(
        'AppUser',
        back_populates='mood_survey_responses',
    )
    mood = Column(Integer)
    energy = Column(Integer)
    adderall_crash = Column(Integer)
    sleep_hours = Column(Float)
    date_time = Column(
        DateTime,
        primary_key=True,
    )

class AppUser(Base):
    __tablename__ = 'app_user'
    id = Column(Integer, primary_key=True)
    mood_survey_responses = relationship(
        'MoodSurveyResponse',
        back_populates='app_user',
    )
    sleep_survey_responses = relationship(
        'SleepSurveyResponse',
        back_populates='app_user',
    )
    weigh_ins = relationship(
        'WeighIn',
        back_populates='app_user',
    )
    loseit_foods = relationship(
        'LoseitFood',
        back_populates='app_user',
    )
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
