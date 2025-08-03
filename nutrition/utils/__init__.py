from .nutrition_calculator import calculate_nutrition
from .emphasis_rules import check_emphasis
from .comment_generator import generate_comment
from .food_lookup import fetch_food_name

__all__ = [
    "calculate_nutrition",
    "check_emphasis",
    "generate_comment",
    "fetch_food_name"
]

def serialize_model(model):
    return {column.name: getattr(model, column.name) for column in model.__table__.columns}
