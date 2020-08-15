from flask import Flask
from ..config import AppConfig
from flask_login import LoginManager
from ..backend.crud import db_session


login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(AppConfig)

    app.session = db_session
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from . import user_loader

        return app
