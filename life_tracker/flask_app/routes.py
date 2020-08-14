from . import (
    app,
)
from .forms import (
    LoginForm,
)
from ..backend.models import (
    AppUser,
)
from ..backend.crud import (
    contextual_session,
)
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
)
from flask_login import (
    current_user,
    login_user,
)


@app.route('/')
@app.route('/index')
def index():
    user = current_user
    title = 'LifeTracker'

    template_vars = {
        'user': current_user,
        'title': title,
    }

    return render_template('index.html', **template_vars)

@app.route('/login', methods=['GET', 'POST'])
def login():
    failed_login_message = 'Invalid username or password.'
    # We don't need to log in a user who's already logged in
    if current_user.is_authenticated:
        return(redirect(url_for('index')))

    # The user has submitted a login form, if they exist log them in
    # otherwise, give a generic and unhelpful error (to avoid exploits)
    form = LoginForm()
    if form.validate_on_submit():
        user = app.session.query(AppUser).filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash(failed_login_message)
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    
    # The user has not submitted a login form, therefore render it unto them
    return render_template(
        'login.html',
        title='Sign In',
        form=form
    )
