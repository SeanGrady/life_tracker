from sqlalchemy.dialects.postgresql import insert
from datetime import datetime
from sqlalchemy import (
    Table,
    MetaData,
)
from .models import Base
from .crud import contextual_session


def create_mirrored_table(name, base_table):
    meta = MetaData()
    columns = [
        column.copy()
        for column in base_table.columns
    ]
    mirrored_table = Table(
        name,
        meta,
        *columns,
    )
    return mirrored_table


def insert_dataframe_ignore_duplicates(dataframe, orm_table):
    database_table = orm_table.__table__

    tablename_datetime_format = '%Y%m%d_%H%M%S'
    temp_table_name = (
        database_table.name
        + '_temporary_{}'.format(datetime.now().strftime(tablename_datetime_format))
    )
    # create the temporary table
    temp_table = create_mirrored_table(temp_table_name, database_table)

    with contextual_session() as session:

        connection = session.get_bind()
        temp_table.create(connection)
        

        dataframe.to_sql(
            temp_table_name,
            if_exists='append',
            index=False,
            con=connection,
        )

        #do the sqlalchemy postgres upsert thing
        insert_statement = insert(
            database_table,
        ).from_select(
            names=temp_table.columns.keys(),
            select=temp_table,
        )

        do_nothing_statement = insert_statement.on_conflict_do_nothing()
        connection.execute(do_nothing_statement)
        temp_table.drop(connection)
