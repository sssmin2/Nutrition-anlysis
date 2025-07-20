from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from db_model import db   
from routes.food import food_bp
from routes.raw import raw_bp
from routes.standard import standard_bp
from routes.ingredients import ingredients_bp

# Flask 앱 초기화
app = Flask(__name__)

# CORS 설정 (모든 도메인 허용)
CORS(app)

# db 설정
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

# sqlalchemy 앱 연결
db.init_app(app)  

# 블루프린트 등록
app.register_blueprint(food_bp)
app.register_blueprint(raw_bp)
app.register_blueprint(standard_bp)
app.register_blueprint(ingredients_bp)

@app.route('/')
def home():
    return 'nutrition api ok'

# 로컬에서만 일단 실행
if __name__ == '__main__':
    app.run(debug=True)