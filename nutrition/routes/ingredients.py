from flask import Blueprint, jsonify, request
from db_model.food_ingredients import FoodIngredients
from utils import serialize_model
from sqlalchemy import func

ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')

# 전체 원재료 조회
@ingredients_bp.route('/', methods=['GET'])
def get_all_ingredients():
    ingredients = FoodIngredients.query.all()
    return jsonify([serialize_model(item) for item in ingredients])

# 특정 원재료 조회 (정확한 대표 원재료명 기준)
@ingredients_bp.route('/name/<string:raw_name>', methods=['GET'])
def get_ingredient_by_name(raw_name):
    item = FoodIngredients.query.filter_by(rprsnt_rawmtrl_nm=raw_name).first()
    if item:
        return jsonify(serialize_model(item))
    else:
        return jsonify({'error': 'Ingredient not found'}), 404

# 원재료명 부분 검색
@ingredients_bp.route('/search', methods=['GET'])
def search_ingredient_by_name():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Query parameter "name" is required'}), 400

    ingredients = FoodIngredients.query.filter(
        func.lower(FoodIngredients.rprsnt_rawmtrl_nm).like(f'%{name.lower()}%')
    ).all()

    if ingredients:
        return jsonify([serialize_model(item) for item in ingredients])
    else:
        return jsonify({'message': 'No matching ingredient found'}), 404
