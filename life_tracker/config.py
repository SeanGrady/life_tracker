import os
from dotenv import load_dotenv
from pathlib import Path


project_directory = Path(__file__).parent.absolute()
flask_env_path = project_directory / '.flaskenv'
backend_env_path = project_directory / '.dbenv'
load_dotenv(dotenv_path=flask_env_path)
load_dotenv(dotenv_path=backend_env_path)


class AppConfig(object):
    DATABASE_URI = os.getenv(
        'DATABASE_URI',
    )
    SECRET_KEY = os.getenv(
        'FLASK_SECRET_KEY',
    )
    FLASK_ENV = os.getenv(
        'FLASK_ENV',
    )
    FLASK_APP = os.getenv(
        'FLASK_APP',
    )
