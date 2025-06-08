from pathlib import Path
from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# データベース接続情報
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# MySQLのURL構築
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SSL_CA_PATH = os.getenv('SSL_CA_PATH')
# カレントディレクトリから絶対パスを取得（安全）
BASE_DIR = Path(__file__).resolve().parent.parent  # ← 1つ上が「backend」フォルダ
SSL_CA_PATH = str(BASE_DIR / "DigiCertGlobalRootCA.crt.pem")

# エンジンの作成
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={
        "ssl_ca": SSL_CA_PATH
    }
)

# 実際に接続してみる（確認用）
try:
    with engine.connect() as connection:
        print("✅ MySQLへの接続に成功しました")
except Exception as e:
    print("❌ 接続に失敗しました")
    print(e)