from life_tracker.backend.gforms_wrapper import (
    download_gforms_responses_for_user,
)
from life_tracker.backend.models import AppUser
from life_tracker.backend.crud import contextual_session

user_id = 1

if __name__ == '__main__':
    download_gforms_responses_for_user(user_id)
