from . import db

class FoodNutritionDB(db.Model):
    __tablename__ = 'food_nutrition_db'
    
    food_code = db.Column(db.String(50), primary_key=True, nullable=False)
    food_name = db.Column(db.String(255), nullable=False)
    serving_size_g = db.Column(db.Integer)
    net_weight_g = db.Column(db.Float)
    calorie_kcal = db.Column(db.Float)
    protein_g = db.Column(db.Float)
    fat_g = db.Column(db.Float)
    carbohydrate_g = db.Column(db.Float)
    sugar_g = db.Column(db.Float)
    sodium_mg = db.Column(db.Float)
    vitamin_a_μg = db.Column(db.Float)
    vitamin_c_mg = db.Column(db.Float)
    vitamin_d_mg = db.Column(db.Float)
    cholesterol_mg = db.Column(db.Float)
    saturated_fat_g = db.Column(db.Float)
    trans_fat_g = db.Column(db.Float)
    vitamin_b12_μg = db.Column(db.Float)
    zinc_mg = db.Column(db.Float)
    
