from ..flask_app import login
from .crud import (
    contextual_session,
)
from .models import AppUser


@login.user_loader
def load_user(id):
    with contextual_session() as session:
        return session.query(AppUser).get(int(id))
