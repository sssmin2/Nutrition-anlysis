def check_emphasis(nutrition_summary):
    """
    강조 조건 기준에 따라 메뉴가 어떤 강조 표현을 충족하는지 판별
    기준: 식품 100g당 또는 100kcal당 기준
    """
    result = {}

    # 총량
    weight = nutrition_summary.get("total_weight_g", 0) or 1  # 0g이면 오류 방지
    kcal = nutrition_summary.get("calorie_kcal", 0) or 1

    # 단위 환산
    per_100g_factor = 100 / weight
    per_100kcal_factor = 100 / kcal

    # per 100g 기준 계산
    per_100g = {k: nutrition_summary.get(k, 0) * per_100g_factor for k in nutrition_summary if k.endswith(('_g', '_mg', '_μg'))}
    per_100kcal = {k: nutrition_summary.get(k, 0) * per_100kcal_factor for k in nutrition_summary if k.endswith(('_g', '_mg', '_μg'))}

    # ===== 기준값 =====
    # 단위: g 또는 mg 또는 μg
    daily_values = {
        "vitamin_b6_mg": 1.5,
        "vitamin_b12_μg": 2.4,
        "vitamin_c_mg": 100,
        "vitamin_d_μg": 10,
        "vitamin_e_mg": 11,
        "vitamin_k_μg": 70,
        "calcium_mg": 700,
        "iron_mg": 12,
        "zinc_mg": 8.5,
        "protein_g": 55,
        "dietary_fiber_g": 25,
    }

    # ===== 함유/풍부 기준 =====
    def check_nutrient_emphasis(nutrient_key, dv):
        contained = (
            per_100g.get(nutrient_key, 0) >= dv * 0.15 or
            per_100kcal.get(nutrient_key, 0) >= dv * 0.05
        )
        rich = (
            per_100g.get(nutrient_key, 0) >= dv * 0.30 or
            per_100kcal.get(nutrient_key, 0) >= dv * 0.10
        )
        return contained, rich

    for label, key in [
        ("비타민 B6", "vitamin_b6_mg"),
        ("비타민 B12", "vitamin_b12_μg"),
        ("비타민 C", "vitamin_c_mg"),
        ("비타민 D", "vitamin_d_μg"),
        ("비타민 E", "vitamin_e_mg"),
        ("비타민 K", "vitamin_k_μg"),
        ("칼슘", "calcium_mg"),
        ("철분", "iron_mg"),
        ("아연", "zinc_mg"),
    ]:
        has, rich = check_nutrient_emphasis(key, daily_values[key])
        if has:
            result[f"{label} 함유"] = True
        if rich:
            result[f"{label} 풍부"] = True

    # ===== 고단백 / 식이섬유 기준 =====
    if (
        per_100g.get("protein_g", 0) >= daily_values["protein_g"] * 0.20 or
        per_100kcal.get("protein_g", 0) >= daily_values["protein_g"] * 0.10
    ):
        result["고단백"] = True

    if (
        per_100g.get("dietary_fiber_g", 0) >= 3 or
        per_100kcal.get("dietary_fiber_g", 0) >= 1.5
    ):
        result["식이섬유 함유"] = True
    if (
        per_100g.get("dietary_fiber_g", 0) >= 6 or
        per_100kcal.get("dietary_fiber_g", 0) >= 3
    ):
        result["식이섬유 풍부"] = True

    # ===== 저감 표현 기준 =====
    if per_100g.get("calorie_kcal", 999) < 40:
        result["저칼로리"] = True

    fat_g = per_100g.get("fat_g", 0)
    sat_fat_g = per_100g.get("saturated_fat_g", 0)
    trans_fat_g = per_100g.get("trans_fat_g", 0)
    cholesterol_mg = per_100g.get("cholesterol_mg", 0)
    sodium_mg = per_100g.get("sodium_mg", 0)
    sugar_g = per_100g.get("sugar_g", 0)

    if fat_g < 3:
        result["저지방"] = True
    if fat_g < 0.5:
        result["무지방"] = True
    if sat_fat_g < 1.5:
        result["저포화지방"] = True
    if sat_fat_g < 0.1:
        result["무포화지방"] = True
    if trans_fat_g < 0.5:
        result["저트랜스지방"] = True
    if cholesterol_mg < 20 and sat_fat_g < 1.5:
        result["저콜레스테롤"] = True
    if cholesterol_mg < 5 and sat_fat_g < 1.5:
        result["무콜레스테롤"] = True
    if sugar_g < 5:
        result["저당류"] = True
    if sugar_g < 0.5:
        result["무당류"] = True
    if sodium_mg < 120:
        result["저나트륨"] = True
    if sodium_mg < 5:
        result["무나트륨"] = True

    return result
