from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lifetracker_config import DATABASE_URI
from models import Base
from contextlib import contextmanager


engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@contextmanager
def scoped_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
