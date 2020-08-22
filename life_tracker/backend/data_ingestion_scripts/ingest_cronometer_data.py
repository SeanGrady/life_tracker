from life_tracker.backend.cronometer import CronometerDataLoader
from life_tracker.backend.crud import contextual_session
from life_tracker.backend.models import AppUser
from pathlib import Path
import argparse


pwd = Path('.')
default_user_id = 1
default_export_directory = pwd / 'data_exports/cronometer_exports'

def ingest_data(user_id, relative_export_directory):
    export_directory = pwd / relative_export_directory
    with contextual_session() as session:
        user = session.query(AppUser).get(user_id)
        loader = CronometerDataLoader(
            user,
            session,
            export_directory,
        )
        loader.load_exports_into_database()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-e',
        '--export_directory',
        help='Relative path to cronometer export directory',
        type=str,
        default=default_export_directory,
    )
    parser.add_argument(
        '-u',
        '--user_id',
        help='User id to put the data under',
        type=int,
        default=default_user_id,
    )
    args = parser.parse_args()
    ingest_data(args.user_id, args.export_directory)
