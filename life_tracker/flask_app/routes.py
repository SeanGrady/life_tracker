from flask_app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Sean',
    }
    title = 'LifeTracker'

    template_vars = {
        'user':user,
        'title':title,
    }

    return render_template('index.html', **template_vars)
