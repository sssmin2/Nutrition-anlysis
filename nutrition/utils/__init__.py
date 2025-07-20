from .nutrition_calculator import calculate_nutrition
from .emphasis_rules import check_emphasis

__all__ = [
    "calculate_nutrition",
    "check_emphasis",
]

def serialize_model(model):
    return {column.name: getattr(model, column.name) for column in model.__table__.columns}
