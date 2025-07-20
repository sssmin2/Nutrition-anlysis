from flask import Blueprint, jsonify, request
from db_model.food_nutrition_db import FoodNutritionDB
from utils import serialize_model
from sqlalchemy import func

food_bp = Blueprint('food', __name__, url_prefix='/food')

# 전체 음식 조회
@food_bp.route('/', methods=['GET'])
def get_all_foods():
    foods = FoodNutritionDB.query.all()
    return jsonify([serialize_model(food) for food in foods])

# 특정 음식 조회 (food_code 기준)
@food_bp.route('/code/<string:food_code>', methods=['GET'])
def get_food_by_code(food_code):
    food = FoodNutritionDB.query.get(food_code)
    if food:
        return jsonify(serialize_model(food))
    else:
        return jsonify({'error': 'Food not found'}), 404
    
# 특정 음식 조회 (food_name 기준 - 전부 일치할 경우)
@food_bp.route('/name/<string:food_name>', methods=['GET'])
def get_food_by_name(food_name):
    food = FoodNutritionDB.query.filter_by(food_name=food_name).first()
    if food:
        return jsonify(serialize_model(food))
    else:
        return jsonify({'error':'Food not Found'}), 404

# 음식 이름으로 부분 검색
@food_bp.route('/search', methods=['GET'])
def search_food_by_name():
    name =  request.args.get('name')
    if not name:
        return jsonify({'error':'Query parameter "naeme" is required'}), 400
    
    # 대소문자 구분 없이 부분 일치 검색
    foods = FoodNutritionDB.query.filter(
        func.lower(FoodNutritionDB.food_name).like(f'%{name.lower()}%')
    ).all()
    
    if foods:
        return jsonify([serialize_model(food) for food in foods])
    else:
        return jsonify({'message':'No matching food found'}), 404