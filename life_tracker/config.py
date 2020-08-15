import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.flaskenv'
load_dotenv(dotenv_path=env_path)


class AppConfig(object):
    DATABASE_URI = os.getenv(
        'DATABASE_URI',
        'postgres+psycopg2://postgres:password@127.0.0.1:5432/lifetracker-test'
    )
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        'no-peeking'
    )
    FLASK_ENV = os.getenv(
        'FLASK_ENV',
    )
    FLASK_APP = os.getenv(
        'FLASK_APP',
    )
