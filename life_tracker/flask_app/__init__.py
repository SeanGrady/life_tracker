from flask import Flask
from ..config import AppConfig
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(AppConfig)
login = LoginManager(app)


from . import routes
