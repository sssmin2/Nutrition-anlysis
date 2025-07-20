from flask import Blueprint, jsonify, request
from db_model.raw_food_nutrition import RawFoodNutrition
from utils import serialize_model
from sqlalchemy import func

raw_bp = Blueprint('raw', __name__, url_prefix='/raw')

# 전체 원재료 식품 조회
@raw_bp.route('/', methods=['GET'])
def get_all_raw_foods():
    raw_foods = RawFoodNutrition.query.all()
    return jsonify([serialize_model(item) for item in raw_foods])

# 특정 원재료 식품조회 (food_code로 조회)
@raw_bp.route('/code/<string:food_code>', methods=['GET'])
def get_raw_food_by_code(food_code):
    item = RawFoodNutrition.query.get(food_code)
    if item:
        return jsonify(serialize_model(item))
    else:
        return jsonify({'error':'Raw food not found'}), 404
    
# 특정 원재료 식품 조회 (food_name으로 조회 - 전부 일치할 경우)
@raw_bp.route('/name/<string:food_name>', methods=['GET'])
def get_raw_food_by_name(food_name):
    item = RawFoodNutrition.query.filter_by(food_name=food_name).first()
    if item:
        return jsonify(serialize_model(item))
    else:
        return jsonify({'error':'Raw food not foung'}), 404

# 원재료 식품 이름으로 부분 검색
@raw_bp.route('/search', methods=['GET'])
def search_raw_food_by_name():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Query parameter "name" is required'}), 404
    
    items = RawFoodNutrition.query.filter(
        func.lower(RawFoodNutrition.food_name).like(f'%{name.lower()}%')
    ).all()
    
    if items:
        return jsonify([serialize_model(item) for item in items])
    else:
        return jsonify({'message': 'No matching raw food found'}), 404