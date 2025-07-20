from . import db

class StandardNutrition(db.Model):
    __tablename__ = 'standard_nutrition'
    
    food_code = db.Column(db.String(50), nullable=False, primary_key=True)
    food_name = db.Column(db.String(255), nullable=False)
    data_pid = db.Column(db.String(50))
    data_pid_name = db.Column(db.String(100))
    serving_size_g = db.Column(db.Integer)
    calorie_kcal = db.Column(db.Integer)
    carbohydrate_g = db.Column(db.Float)
    sugar_g = db.Column(db.Float)
    protein_g = db.Column(db.Float)
    fat_g = db.Column(db.Float)
    saturated_fat_g = db.Column(db.Float)
    trans_fat_g = db.Column(db.Float)
    sodium_mg = db.Column(db.Float)
    cholesterol_mg = db.Column(db.Float)
    fiber_g = db.Column(db.Float)
    vitamin_c_mg = db.Column(db.Float)
    vitamin_d_μg = db.Column(db.Float)
    calcium_mg = db.Column(db.Float)
    iron_mg = db.Column(db.Float)
    