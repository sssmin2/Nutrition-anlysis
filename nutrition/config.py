import os
from dotenv import load_dotenv

# .env 파일의 환경변수 로드
load_dotenv()

# DB 설정
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:00000000@localhost:3306/nutrition'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# AI 모델 연동을 위한 OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")