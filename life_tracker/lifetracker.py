from .flask_app import app
from .backend.crud import contextual_session
from .backend.models import (
    AppUser,
)


@app.shell_context_processor
def make_shell_context():
    with contextual_session() as session:
        context = {
            'session': session,
            'AppUser': AppUser,
        }
        return context
