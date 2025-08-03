from flask import Blueprint, request, jsonify
from db_model.menu import Menu
from db_model.menu_ingredient import MenuIngredient
from utils.food_lookup import fetch_food_name
from utils.nutrition_calculator import calculate_nutrition
from utils.emphasis_rules import check_emphasis
from utils.comment_generator import generate_comment, format_comment_by_sentence
from utils import serialize_model
from sqlalchemy.orm import joinedload
from db_model import db
import re
import traceback

menu_bp = Blueprint('menu', __name__, url_prefix='/menu')


# 메뉴 생성 API
@menu_bp.route('/create', methods=['POST'])
def create_menu():
    data = request.get_json()

    name = data.get('name')
    price = data.get('price')
    ingredients = data.get('ingredients')  # 리스트: [{'food_code': '...', 'amount': 30}, ...]

    # 1. 유효성 검사
    if not name or not isinstance(name, str) or len(name) > 30:
        return jsonify({'error': '메뉴명은 최대 30자의 문자열이어야 합니다.'}), 400

    if not re.fullmatch(r'[가-힣a-zA-Z0-9\s]+', name):
        return jsonify({'error': '메뉴명은 한글, 영문, 숫자, 공백만 포함해야 합니다.'}), 400

    if not isinstance(price, int) or not (500 <= price <= 50000):
        return jsonify({'error': '가격은 500원부터 50,000원 사이의 정수여야 합니다.'}), 400

    if not ingredients or not isinstance(ingredients, list):
        return jsonify({'error': '원재료 리스트가 필요합니다.'}), 400

    if len(ingredients) > 30:
        return jsonify({'error': '최대 30개의 원재료만 선택할 수 있습니다.'}), 400

    for item in ingredients:
        if 'food_code' not in item or 'amount' not in item:
            return jsonify({'error': '원재료 항목에 food_code와 amount가 필요합니다.'}), 400
        if not isinstance(item['amount'], (int, float)) or item['amount'] <= 0:
            return jsonify({'error': '함량은 양의 숫자여야 합니다.'}), 400

    # 2. 메뉴 및 원재료 저장
    try:
        # 메뉴 저장
        new_menu = Menu(name=name, price=price)
        db.session.add(new_menu)
        db.session.flush()  # 메뉴 ID 확보 (아직 commit 안 함)

        # 원재료-함량 저장
        for item in ingredients:
            ingredient = MenuIngredient(
                menu_id=new_menu.id,
                food_code=item['food_code'],
                amount=item['amount']
            )
            db.session.add(ingredient)

        db.session.commit()
        return jsonify({'message': '메뉴가 생성되었습니다.', 'menu_id': new_menu.id}), 201

    except Exception as e:
        db.session.rollback()
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# 메뉴 단건 조회
@menu_bp.route('/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    # 메뉴 기본 정보
    menu_data = serialize_model(menu)

    # 해당 메뉴의 원재료 조회
    ingredient_list = []
    for item in MenuIngredient.query.filter_by(menu_id=menu.id).all():
        ingredient_list.append({
            'food_code': item.food_code,
            'food_name': fetch_food_name(item.food_code),
            'amount': item.amount
        })

    # 원재료 정보 추가
    menu_data['ingredients'] = ingredient_list

    return jsonify(menu_data)


# 전체 메뉴 리스트 조회
@menu_bp.route('/', methods=['GET'])
def get_all_menus():
    menus = Menu.query.all()

    result = []
    for menu in menus:
        menu_data = serialize_model(menu)

        # 원재료 개수 계산
        ingredient_count = MenuIngredient.query.filter_by(menu_id=menu.id).count()
        menu_data['ingredient_count'] = ingredient_count

        result.append(menu_data)

    return jsonify(result)

# 메뉴 영양 분석
@menu_bp.route('/analyze/<int:menu_id>', methods=['GET'])
def analyze_menu(menu_id):
    menu = Menu.query.options(joinedload(Menu.ingredients)).filter_by(id=menu_id).first()

    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    # 영양분 계산
    result = calculate_nutrition(menu)

    return jsonify(result)

# 강조 조건 판단
@menu_bp.route('/emphasis/<int:menu_id>', methods=['GET'])
def get_menu_emphasis(menu_id):
    # 메뉴 조회 및 재료 조인
    menu = Menu.query.options(joinedload(Menu.ingredients)).filter_by(id=menu_id).first()
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    # 영양 정보 계산
    nutrition_summary = calculate_nutrition(menu)

    # 강조 조건 판단
    emphasis_result = check_emphasis(nutrition_summary)

    return jsonify({
        'menu_id': menu.id,
        'menu_name': menu.name,
        'emphasis': emphasis_result
    })



# AI 코멘트 생성
@menu_bp.route('/comment/<int:menu_id>', methods=['GET'])
def get_menu_comment(menu_id):

    # 메뉴 + 재료 로딩
    menu = Menu.query.options(joinedload(Menu.ingredients)).filter_by(id=menu_id).first()
    if not menu:
        return jsonify({'error': 'Menu not found'}), 404

    # 영양성분 계산
    nutrition = calculate_nutrition(menu)

    # 원재료 이름 리스트 추출
    ingredient_names = [
        fetch_food_name(ing.food_code) or ing.food_code
        for ing in menu.ingredients
    ]
    
    # AI 코멘트 생성
    try:
        comment_raw = generate_comment(
            menu_name=menu.name,
            ingredients=ingredient_names,
            nutrients=nutrition
        )
        comment = format_comment_by_sentence(comment_raw)

    except Exception as e:
        return jsonify({'error': f'AI 코멘트 생성 실패: {str(e)}'}), 500

    return jsonify({
        'menu_id': menu.id,
        'menu_name': menu.name,
        'comment': comment
    })