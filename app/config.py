import os
from urllib.parse import quote_plus

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")
    _database_url = os.getenv("DATABASE_URL")

    if _database_url:
        SQLALCHEMY_DATABASE_URI = _database_url
    else:
        db_user = os.getenv("DB_USER", "root")
        db_password = quote_plus(os.getenv("DB_PASSWORD", "password"))
        db_host = os.getenv("DB_HOST", "localhost")
        db_port = os.getenv("DB_PORT", "3306")
        db_name = os.getenv("DB_NAME", "hotel_listing")
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
