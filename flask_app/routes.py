from flask_app import app


@app.route('/')
@app.route('/index')
def index():
    return "It's a flask app!"