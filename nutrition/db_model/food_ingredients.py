from . import db

class FoodIngredients(db.Model):
    __tablename__ = 'food_ingredients'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    rprsnt_rawmtrl_nm = db.Column(db.Text)
    rawmtrl_ncknm = db.Column(db.Text)
    eng_nm = db.Column(db.Text)
    lclas_nm = db.Column(db.Text)
    mlsfc_nm = db.Column(db.Text)