from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base
from contextlib import contextmanager
from sqlalchemy.dialects.postgresql import insert


engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


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
