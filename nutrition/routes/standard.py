from flask import Blueprint, jsonify, request
from db_model.standard_nutrition import StandardNutrition
from utils import serialize_model
from sqlalchemy import func

standard_bp = Blueprint('standard', __name__, url_prefix='/standard')

# 전체 표준 식품 조회
@standard_bp.route('/', methods=['GET'])
def get_all_standard_foods():
    foods = StandardNutrition.query.all()
    return jsonify([serialize_model(food) for food in foods])

# 특정 식품 조회 (food_code 기준)
@standard_bp.route('/code/<string:food_code>', methods=['GET'])
def get_standard_food_by_code(food_code):
    food = StandardNutrition.query.get(food_code)
    if food:
        return jsonify(serialize_model(food))
    else:
        return jsonify({'error': 'Standard food not found'}), 404
    
# 특정 식품 조회 (food_name 기준 - 전부 일치한 경우)
@standard_bp.route('/name/<string:food_name>', methods=['GET'])
def get_standard_food_by_name(food_name):
    food = StandardNutrition.query.filter_by(food_name=food_name).first()
    if food:
        return jsonify(serialize_model(food))
    else:
        return jsonify({'error': 'Standard food not found'}), 404

# 식품 이름으로 부분 검색
@standard_bp.route('/search', methods=['GET'])
def search_standard_food_by_name():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Query parameter "name" is required'}), 400
    
    foods = StandardNutrition.query.filter(
        func.lower(StandardNutrition.food_name).like(f'%{name.lower()}%')
    ).all()
    
    if foods:
        return jsonify([serialize_model(food) for food in foods])
    else:
        return jsonify({'message': 'No matching standard food found'}), 404
    