from models import (
    CronometerServing,
    DailyNutritionReport,
    LoseitFood,
)
from ..crud import (
    contextual_session,
    get_or_create,
)


def create_daily_nutrition_reports():
    with contextual_session() as session:
        cronometer_servings = session.query(
            CronometerServing
        )
        loseit_foods = session.query(
            LoseitFood,
        )

        for serving in cronometer_servings:
            daily_report = get_or_create(
                session,
                DailyNutritionReport,
                date=serving.day,
                app_user_id=serving.app_user_id,
            ) 
            daily_report.update(
                calories=serving.energy_kcal
            )

        for food in loseit_foods:
            daily_report = get_or_create(
                session,
                DailyNutritionReport,
                date=food.raw_date,
                app_user_id=serving.app_user_id,
            )
            daily_report.udpate(
                calories=food.raw_calories,
            )
