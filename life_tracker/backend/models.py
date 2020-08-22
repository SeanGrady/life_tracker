from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Float,
    DateTime,
    Time,
    Boolean,
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


class CronometerLogExportMixin(object):
    """
    Mixin for Cronometer log-type exports -- i.e. those with a separate 'Date'
    and 'Time' column. The summary type exports (currently only one) only have
    a 'Date' column.
    """
    @declared_attr
    def time(cls):
        return Column(
            Time,
            nullable=False,
            primary_key=True,
        )
    
    @declared_attr
    def day(cls):
        return Column(
            Date,
            nullable=False,
            primary_key=True,
        )

    @declared_attr
    def group(cls):
        return Column(
            String,
            nullable=False,
            primary_key=True,
        )

class CronometerExercise(Base, AppUserMixin, CronometerLogExportMixin):
    __tablename__ = 'cronometer_exercise'
    exercise = Column(
        String,
        nullable=False,
        primary_key=True,
    )
    minutes = Column(Float)
    calories_burned = Column(Float)


class CronometerNote(Base, AppUserMixin, CronometerLogExportMixin):
    __tablename__ = 'cronometer_note'
    note = Column(
        String,
        nullable=False,
    )


class CronometerBiometric(Base, AppUserMixin, CronometerLogExportMixin):
    __tablename__ = 'cronometer_biometric'
    metric = Column(
        String,
        nullable=False,
    )
    unit = Column(String)
    amount = Column(Float)


class CronometerDailySummary(Base, AppUserMixin):
    __tablename__ = 'cronometer_daily_summary'
    date = Column(
        Date,
        nullable=False,
        primary_key=True,
    )
    completed = Column(Boolean)

    energy_kcal = Column(Float)
    alcohol_g = Column(Float)
    caffeine_mg = Column(Float)
    water_g = Column(Float)
    b1_thiamine_mg = Column(Float)
    b2_riboflavin_mg = Column(Float)
    b3_niacin_mg = Column(Float)
    b5_pantothenic_acid_mg = Column(Float)
    b6_pyridoxine_mg = Column(Float)
    b12_cobalamin_ug = Column(Float)
    folate_ug = Column(Float)
    vitamin_a_iu = Column(Float)
    vitamin_c_mg = Column(Float)
    vitamin_d_iu = Column(Float)
    vitamin_e_mg = Column(Float)
    vitamin_k_ug = Column(Float)
    calcium_mg = Column(Float)
    copper_mg = Column(Float)
    iron_mg = Column(Float)
    magnesium_mg = Column(Float)
    manganese_mg = Column(Float)
    phosphorus_mg = Column(Float)
    potassium_mg = Column(Float)
    selenium_ug = Column(Float)
    sodium_mg = Column(Float)
    zinc_mg = Column(Float)
    carbs_g = Column(Float)
    fiber_g = Column(Float)
    starch_g = Column(Float)
    sugars_g = Column(Float)
    net_carbs_g = Column(Float)
    fat_g = Column(Float)
    cholesterol_mg = Column(Float)
    monounsaturated_g = Column(Float)
    polyunsaturated_g = Column(Float)
    saturated_g = Column(Float)
    trans_fats_g = Column(Float)
    omega_3_g = Column(Float)
    omega_6_g = Column(Float)
    cystine_g = Column(Float)
    histidine_g = Column(Float)
    isoleucine_g = Column(Float)
    leucine_g = Column(Float)
    lysine_g = Column(Float)
    methionine_g = Column(Float)
    phenylalanine_g = Column(Float)
    protein_g = Column(Float)
    threonine_g = Column(Float)
    tryptophan_g = Column(Float)
    tyrosine_g = Column(Float)
    valine_g = Column(Float)


class CronometerServing(Base, AppUserMixin, CronometerLogExportMixin):
    __tablename__ = 'cronometer_serving'

    food_name = Column(
	String,
	nullable=False,
	primary_key=True,
    )
    amount = Column(
        String,
        nullable=False,
        primary_key=True,
    )
    category = Column(String)

    energy_kcal = Column(Float)
    alcohol_g = Column(Float)
    caffeine_mg = Column(Float)
    water_g = Column(Float)
    b1_thiamine_mg = Column(Float)
    b2_riboflavin_mg = Column(Float)
    b3_niacin_mg = Column(Float)
    b5_pantothenic_acid_mg = Column(Float)
    b6_pyridoxine_mg = Column(Float)
    b12_cobalamin_ug = Column(Float)
    folate_ug = Column(Float)
    vitamin_a_iu = Column(Float)
    vitamin_c_mg = Column(Float)
    vitamin_d_iu = Column(Float)
    vitamin_e_mg = Column(Float)
    vitamin_k_ug = Column(Float)
    calcium_mg = Column(Float)
    copper_mg = Column(Float)
    iron_mg = Column(Float)
    magnesium_mg = Column(Float)
    manganese_mg = Column(Float)
    phosphorus_mg = Column(Float)
    potassium_mg = Column(Float)
    selenium_ug = Column(Float)
    sodium_mg = Column(Float)
    zinc_mg = Column(Float)
    carbs_g = Column(Float)
    fiber_g = Column(Float)
    starch_g = Column(Float)
    sugars_g = Column(Float)
    net_carbs_g = Column(Float)
    fat_g = Column(Float)
    cholesterol_mg = Column(Float)
    monounsaturated_g = Column(Float)
    polyunsaturated_g = Column(Float)
    saturated_g = Column(Float)
    trans_fats_g = Column(Float)
    omega_3_g = Column(Float)
    omega_6_g = Column(Float)
    cystine_g = Column(Float)
    histidine_g = Column(Float)
    isoleucine_g = Column(Float)
    leucine_g = Column(Float)
    lysine_g = Column(Float)
    methionine_g = Column(Float)
    phenylalanine_g = Column(Float)
    protein_g = Column(Float)
    threonine_g = Column(Float)
    tryptophan_g = Column(Float)
    tyrosine_g = Column(Float)
    valine_g = Column(Float)
