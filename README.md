# 🥗 Nutrition Analysis System(팀 골고루 기업과제)

건강한 식단 구성을 돕기 위해, **영양성분 자동 분석**, **영양 강조 표시**, **AI 기반 요약 코멘트**를 제공하는 웹/모바일 통합 시스템입니다.  
사용자는 직접 메뉴를 생성하고, 원재료를 구성하여 전체 영양 분석을 확인할 수 있습니다.

---

## 📍 Introduction

본 프로젝트는 다음과 같은 목표를 가지고 있습니다

- 메뉴에 사용된 **원재료 기준 영양성분 자동 계산**
- 식품의약품안전처 기준에 따라 **저칼로리, 고단백 등 강조 조건 판단**
- AI 모델(GPT)을 활용하여 **건강 코멘트 자동 생성**
- Flutter 앱과 Flask 백엔드로 구현한 API 기반 구조

---

## 🖇️ Documents

### 🕒 기간

| 구분 | 내용 |
|------|------|
| 프로젝트 시작일 | 2025년 7월 2일 |
| 1차 완료 목표일 | 2025년 8월 중순 |

### ⚙️ 개발 흐름

1. 요구사항 설계 및 기능 정의  
2. 공공데이터 수집 (식품영양성분 DB, API 연동 포함)  
3. 영양소 데이터 전처리 및 정규화  
4. MySQL 기반 DB 설계 및 구축  
5. Flask API 개발 (CRUD + 분석 + 강조 조건 + 코멘트)  
6. Flutter 앱 연동 (메뉴 생성 및 분석 인터페이스 제공)  
7. OpenAI GPT 기반 AI 코멘트 생성 기능 통합  
8. 테스트 및 기능 개선 반복

### 📑 주요 API 명세서

###
| 메서드  | 경로                         | 설명           |
| ---- | -------------------------- | ------------ |
| GET  | `/`                        | 서버 상태 확인     |
| POST | `/menu/create`             | 메뉴 생성        |
| GET  | `/menu/`                   | 전체 메뉴 리스트 조회 |
| GET  | `/menu/<menu_id>`          | 특정 메뉴 상세 조회  |
| GET  | `/menu/analyze/<menu_id>`  | 영양 분석        |
| GET  | `/menu/emphasis/<menu_id>` | 강조 조건 조회     |
| GET  | `/menu/comment/<menu_id>`  | AI 건강 코멘트    |
| GET  | `/search/all?name=`        | 식품 통합 검색     |

> [BE 전체 API 명세서보기]

---

## 🎥 DEMO or PRTOTYPE

> (삽입예정)

- Flutter 앱 시연 영상
- API 호출 흐름
- 강조 조건 및 코멘트 생성 결과 예시

---

## 🛠 Tech Stack

### [BE]
- **Python 3.10**
- **Flask**: RESTful API 서버
- **SQLAlchemy**: ORM 및 DB 연동
- **OpenAI GPT API**: AI 문장 생성
- **dotenv**: 기본 설정

### [FE]
- **Flutter**: 크로스 플랫폼 앱 (iOS / Android)
- **Dart**: Flutter 기반 언어
- **Riverpod**: 상태 관리
- **http / dio**: API 통신

### [Infra & Tools]
- **MySQL**: 영양성분 데이터베이스
- **Postman**: API 테스트 및 문서화
- **Git / GitHub**: 형상관리 및 이슈 관리
- **GitHub Actions (예정)**: CI/CD 자동화

---

## 🗂️ Database

### 📌 ERD 구조

ERD 나타낼 예정

---

## 💻 System Architecture
나타낼 예정

---

## 📂 Project Structure

### 
    NUTRITION[BE]/
    ├── db_model/                         # SQLAlchemy 모델 정의 디렉터리
    │   ├── __init__.py                   # 모델 초기화 및 연결
    │   ├── food_ingredients.py           # 원재료 구성 정보 (예: 메뉴에 포함된 식품)
    │   ├── food_nutrition_db.py          # 식품별 영양성분 DB (가공된 데이터 기준)
    │   ├── menu.py                       # 메뉴 테이블 모델
    │   ├── menu_ingredient.py            # 메뉴-원재료 연결 테이블
    │   ├── raw_food_nutrition.py         # 원시 영양소 수치 원본 (공공데이터 원형)
    │   └── standard_nutrition.py         # 영양 강조 기준 (100g, 100kcal 기준치 저장용)
    │
    ├── routes/                           # Flask Blueprint 라우터 정의
    │   ├── __init__.py
    │   ├── food.py                       # 식품 데이터 API (단일 식품, 전체 조회 등)
    │   ├── ingredients.py                # 원재료 관련 API (추가/수정 등)
    │   ├── menu.py                       # 메뉴 CRUD + 분석 API (중심 API)
    │   ├── raw.py                        # 원시 데이터 조회용 API
    │   └── standard.py                   # 기준 영양값 관련 API (강조 기준값 관리 등)
    │
    ├── utils/                            # 기능 유틸리티 함수 모음
    │   ├── __init__.py
    │   ├── comment_generator.py          # OpenAI GPT API 기반 AI 코멘트 생성기
    │   ├── emphasis_rules.py             # 강조 조건 판단 (저지방, 고단백 등 rule-based)
    │   └── nutrition_calculator.py       # 메뉴 전체 영양성분 계산기 (g 기준)
    │
    ├── .env                              # 환경변수 파일
    ├── config.py                         # Flask 앱 설정 (DB URL, GPT 설정 등)
    ├── main.py                           # Flask 앱 진입점 (Blueprint 등록, 서버 실행)

