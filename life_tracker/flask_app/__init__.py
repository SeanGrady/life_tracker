from flask import Flask
from ..config import AppConfig
from flask_login import LoginManager
from ..backend.crud import db_session


app = Flask(__name__)
app.config.from_object(AppConfig)
login = LoginManager(app)

from . import user_loader

app.session = db_session

from . import routes
