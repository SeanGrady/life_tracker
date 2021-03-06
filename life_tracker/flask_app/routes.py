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
    current_app as app,
    render_template,
    flash,
    redirect,
    url_for,
)
from flask_login import (
    current_user,
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
