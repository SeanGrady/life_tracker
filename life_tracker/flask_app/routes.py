from flask_app import (
    app,
)
from flask_app.forms import (
    LoginForm,
)
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
)


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            'Login requested for user {}, remember_me={}'.format(
                form.username.data,
                form.remember_me.data,
            )
        )
        return redirect(url_for('index'))
    return render_template(
        'login.html',
        title='Sign In',
        form=form
    )
