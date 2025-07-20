from db_model.food_nutrition_db import FoodNutritionDB

# 성분 계산 함수
def calculate_nutrition(menu):
    # 분석할 주요 영양소 키
    nutrient_keys = [
        'calorie_kcal',       # 에너지 (kcal)
        'carbohydrate_g',     # 탄수화물 (g)
        'sugar_g',            # 당류 (g)
        'protein_g',          # 단백질 (g)
        'fat_g',              # 지방 (g)
        'saturated_fat_g',    # 포화지방 (g)
        'trans_fat_g',        # 트랜스지방 (g)
        'sodium_mg',          # 나트륨 (mg)
        'cholesterol_mg'      # 콜레스테롤 (mg)
    ]

    # 성분 총합 초기화
    total_nutrients = {key: 0.0 for key in nutrient_keys}
    total_weight = 0.0  # 총 제공량 (g)

    # 메뉴의 각 원재료를 기준으로 계산
    for ingredient in menu.ingredients:
        food = FoodNutritionDB.query.get(ingredient.food_code)
        if not food:
            continue

        # 기준 제공량이 없으면 100g 가정
        base_serving = food.serving_size_g or 100.0

        # 사용량 대비 비율
        ratio = ingredient.amount / base_serving
        total_weight += ingredient.amount

        for key in nutrient_keys:
            value = getattr(food, key, 0.0)
            if value:
                total_nutrients[key] += value * ratio

    # 결과 정리
    result = {
        'menu_id': menu.id,
        'menu_name': menu.name,
        'total_weight_g': round(total_weight, 2),
        **{key: round(total_nutrients[key], 2) for key in nutrient_keys}
    }

    return result
