from .forms import (
    LoginForm,
    RegistrationForm,
)
from flask import (
    current_app as app,
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
)
from flask_login import (
    current_user,
    login_user,
    logout_user,
    login_required,
)
from .. import (
    login_manager
)
from ...backend.models import AppUser


auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static',
)


@login_manager.user_loader
def load_user(id):
    return app.session.query(AppUser).get(int(id))


def unauthorized():
    flash('You must be logged in to view that page')
    return redirect(url_for('home_bp.login'))


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    failed_login_message = 'Invalid email or password.'
    # We don't need to log in a user who's already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home_bp.index'))

    # The user has submitted a login form, if they exist log them in
    # otherwise, give a generic and unhelpful error (to avoid exploits)
    form = LoginForm()
    if form.validate_on_submit():
        user = app.session.query(AppUser).filter_by(email=form.email.data).first()

        if user is None or not user.check_password(form.password.data):
            flash(failed_login_message)
            return redirect(url_for('auth_bp.login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home_bp.index'))
    
    # The user has not submitted a login form, therefore render it unto them
    return render_template(
        'login.html',
        title='Sign In',
        form=form
    )


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home_bp.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = AppUser(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        app.session.add(user)
        app.session.commit()
        flash('Welcome {}, you are now a registerd user!'.format(user.first_name))
        return redirect(url_for('auth_bp.login'))

    return render_template('register.html', title='Register', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
