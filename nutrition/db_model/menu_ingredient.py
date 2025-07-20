from . import db
from sqlalchemy.orm import relationship

class MenuIngredient(db.Model):
    __tablename__ = 'menu_ingredient'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    food_code = db.Column(db.String(50), db.ForeignKey('food_nutrition_db.food_code'), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    menu = relationship('Menu', backref='ingredients')

    def __repr__(self):
        return f'<MenuIngredient food_code={self.food_code} amount={self.amount}g>'
