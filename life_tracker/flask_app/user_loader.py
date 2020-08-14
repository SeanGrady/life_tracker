from . import (
    login,
    app,
)
from ..backend.crud import (
    contextual_session,
)
from ..backend.models import AppUser


@login.user_loader
def load_user(id):
    return app.session.query(AppUser).get(int(id))
