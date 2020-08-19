from life_tracker.flask_app import create_app
from life_tracker.backend.models import *
from flask import current_app as app
from flask_login import current_user, login_user


app = create_app()


@app.shell_context_processor
def make_shell_context():
    context = {
        'app': app,
        'current_user': current_user,
        'AppUser': AppUser,
    }
    return context


if __name__ == "__main__":
    app.run(host='0.0.0.0')
