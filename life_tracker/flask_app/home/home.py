from flask import (
    current_app as app,
    Blueprint,
    render_template,
)
from flask_login import (
    current_user,
)


home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static',
)


@home_bp.route('/')
@home_bp.route('/index')
def index():
    user = current_user

    template_vars = {
        'user': current_user,
    }

    return render_template('index.html', **template_vars)
