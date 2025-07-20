from . import db

class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)  # 한글, 영문, 숫자, 공백 허용
    price = db.Column(db.Integer, nullable=False)    # 비용: 500 ~ 50,000 사이

    # 메뉴 생성일 
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Menu {self.name}>'
