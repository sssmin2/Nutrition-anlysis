# utils/comment_generator.py

import os
import openai

# 환경 변수에서 API 키 불러오기
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_comment(nutrition_data: dict, emphasis_result: dict = None) -> str:
    """
    OpenAI GPT API를 호출하여 AI 기반 코멘트를 생성합니다.
    """

    # 프롬프트 구성
    menu_name = nutrition_data.get("menu_name", "이 메뉴")
    emphasis_labels = list(emphasis_result.keys()) if emphasis_result else []

    prompt = f"""
'{menu_name}'이라는 메뉴의 영양성분은 다음과 같습니다:

총 열량: {nutrition_data.get("calorie_kcal", 0)} kcal
탄수화물: {nutrition_data.get("carbohydrate_g", 0)} g
단백질: {nutrition_data.get("protein_g", 0)} g
지방: {nutrition_data.get("fat_g", 0)} g
포화지방: {nutrition_data.get("saturated_fat_g", 0)} g
트랜스지방: {nutrition_data.get("trans_fat_g", 0)} g
당류: {nutrition_data.get("sugar_g", 0)} g
나트륨: {nutrition_data.get("sodium_mg", 0)} mg
콜레스테롤: {nutrition_data.get("cholesterol_mg", 0)} mg
식이섬유: {nutrition_data.get("dietary_fiber_g", 0)} g

강조 조건: {', '.join(emphasis_labels) if emphasis_labels else '없음'}

위 데이터를 바탕으로, 메뉴의 영양적 특성과 장점, 주의사항 등을 포함한 300자 이내의 한글 건강 코멘트를 작성해주세요.
"""

    # GPT 호출
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 영양 전문가입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
        )
        return response.choices[0].message['content'].strip()

    except Exception as e:
        return f"[AI 응답 실패] {str(e)}"
