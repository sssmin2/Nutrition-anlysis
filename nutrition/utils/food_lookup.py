from db_model.raw_food_nutrition import RawFoodNutrition
from db_model.food_nutrition_db import FoodNutritionDB
from db_model.standard_nutrition import StandardNutrition

def fetch_food_name(food_code: str) -> str | None:
    """
    주어진 food_code에 대해 Raw -> DB -> Standard 순으로 조회하여
    첫 발견된 food_name을 반환합니다.
    """
    for Model in (RawFoodNutrition, FoodNutritionDB, StandardNutrition):
        rec = Model.query.get(food_code)
        if rec and getattr(rec, 'food_name', None):
            return rec.food_name
    return None
