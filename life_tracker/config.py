import os


class AppConfig(object):
    DATABASE_URI = os.getenv(
        'DATABASE_URI',
        'postgres+psycopg2://postgres:password@127.0.0.1:5432/lifetracker-test'
    )
    SECRET_KEY = os.getenv(
        'SECRET_KEY',
        'no-peeking'
    )
