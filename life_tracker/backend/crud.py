from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    scoped_session,
)
from ..config import AppConfig
from .models import Base
from contextlib import contextmanager
from sqlalchemy.dialects.postgresql import insert

from alembic.config import Config
from alembic import command
"""
doing:

import alembic

and then using

alembic.config.Config

does not work, the above is the way their documentation suggests you do this.
Since it's not an issue with relative/absolute imports on my end, as the same
thing happens in the python shell in any directory/package, clearly they're
doing some import-related shenanigans.
"""

from pathlib import Path


engine = create_engine(AppConfig.DATABASE_URI)
Session = sessionmaker(bind=engine)
alembic_config_path = AppConfig.PROJECT_DIRECTORY / 'backend/alembic.ini'


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    alembic_cfg = Config(alembic_config_path)
    command.stamp(alembic_cfg, "head")


@contextmanager
def contextual_session(*args, **kwargs):
    session = Session(*args, **kwargs)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


db_session = scoped_session(sessionmaker(bind=engine))


def insert_if_not_exists(session, model, rows):
    table = model.__table__

    stmt = insert(table).values(rows)

    on_conflict_stmt = stmt.on_conflict_do_nothing(
        index_elements=table.primary_key.columns,
    )
    session.execute(on_conflict_stmt)


if __name__ == "__main__":
    from models import *
    with contextual_session() as session:
        import pdb;pdb.set_trace()
        pass
