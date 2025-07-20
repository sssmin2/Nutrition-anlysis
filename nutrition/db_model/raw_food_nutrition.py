from . import db

class RawFoodNutrition(db.Model):
    __tablename__ = 'raw_food_nutrition'
    
    food_code = db.Column(db.String(50), primary_key=True, nullable=False)
    food_name = db.Column(db.String(255), nullable=False)
    data_pid = db.Column(db.String(50))
    data_pid_name = db.Column(db.String(100))
    serving_size_g = db.Column(db.Integer)
    calorie_kcal = db.Column(db.Integer)
    carbohydrate_g = db.Column(db.Float)
    protein_g = db.Column(db.Float)
    fat_g = db.Column(db.Float)
    sugar_g = db.Column(db.Float)
    saturated_fat_g = db.Column(db.Float)
    trans_fat_g = db.Column(db.Float)
    sodium_mg = db.Column(db.Float)
    cholesterol_mg = db.Column(db.Float)
    dietary_fiber_g = db.Column(db.Float)
    vitamin_a_μg = db.Column(db.Float)
    vitamin_c_mg = db.Column(db.Float)
    vitamin_d_ug = db.Column(db.Float)
    calcium_mg = db.Column(db.Float)
    iron_mg = db.Column(db.Float)
    