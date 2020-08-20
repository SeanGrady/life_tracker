import pandas as pd
from .crud import contextual_session


def snake_case_cronometer_column_name(column_name):
    column_name = column_name.replace(
        ') (',
        '_',
    )
    column_name = column_name.replace(
        ' (',
        '_',
    )
    column_name = column_name.replace(
        ')',
        '',
    )
    column_name = column_name.replace(
        ' ',
        '_',
    )
    column_name = column_name.replace(
        '-',
        '_',
    )
    column_name = column_name.lower()
    return column_name

class CronometerDataLoader(object):
    def __init__(self, user, export_directory):
        self.user = user
        self.export_directory = export_directory
        self.exercise_export_filename = 'exercises.csv'

    def load_exercise_data(self):
        exercise_csv = self.export_directory / self.exercise_export_filename
        exercise_data = pd.load_csv(exercise_csv)
