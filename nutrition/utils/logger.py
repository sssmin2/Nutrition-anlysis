import logging
import os
from logging.handlers import RotatingFileHandler

# 1. 로그 디렉터리 설정 (환경변수 LOG_DIR 있으면 그것을, 없으면 'logs' 디폴트)
LOG_DIR = os.getenv('LOG_DIR', 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# 2. 로거 생성 및 기본 레벨 설정
logger = logging.getLogger('nutrition_app')
logger.setLevel(logging.DEBUG)  
# → 운영 환경에서는 INFO 또는 WARNING 으로 낮추고,
#    개발 환경에서는 DEBUG 로 두면 내부 흐름을 더 상세히 볼 수 있습니다.

# 3. 핸들러 정의

# 3.1 콘솔 핸들러: 화면에 출력 (DEBUG 이상)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 3.2 파일 핸들러: logs/app.log 파일에 기록 (INFO 이상), 회전형
file_handler = RotatingFileHandler(
    filename=os.path.join(LOG_DIR, 'app.log'),
    maxBytes=10 * 1024 * 1024,  # 10 MB
    backupCount=5,              # 옛날 파일 5개까지 보관
    encoding='utf-8'
)
file_handler.setLevel(logging.INFO)

# 4. 포맷터 설정
fmt = '%(asctime)s %(levelname)-8s [%(name)s:%(lineno)d] %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(fmt, datefmt)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 5. 핸들러를 로거에 추가
logger.addHandler(console_handler)
logger.addHandler(file_handler)
