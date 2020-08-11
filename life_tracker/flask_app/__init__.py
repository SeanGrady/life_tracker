from flask import Flask
from life_tracker.config import AppConfig


app = Flask(__name__)
app.config.from_object(AppConfig)


from flask_app import routes
