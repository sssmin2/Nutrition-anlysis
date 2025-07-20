from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy 객체 생성
db = SQLAlchemy()

# 각 테이블 모델 import
from .food_nutrition_db import FoodNutritionDB
from .food_ingredients import FoodIngredients
from .raw_food_nutrition import RawFoodNutrition
from .standard_nutrition import StandardNutrition