import pandas as pd
from .crud import contextual_session
from .models import (
    CronometerNote,
    CronometerDailySummary,
    CronometerExercise,
    CronometerServing,
    CronometerBiometric,
)


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
    column_name = column_name.replace(
        'µ',
        'u',
    )
    column_name = column_name.lower()
    return column_name

class CronometerDataLoader(object):
    def __init__(self, user, session, export_directory):
        self.user = user
        self.session = session
        self.export_directory = export_directory
        self.export_types = [
            'exercise',
            'biometric',
            'serving',
            'note',
            'daily_summary',
        ]
        self.export_models = {
            'exercise': CronometerExercise,
            'biometric': CronometerBiometric,
            'serving': CronometerServing,
            'note': CronometerNote,
            'daily_summary': CronometerDailySummary,
        }
        self.export_filenames = {
            'exercise': 'exercises.csv',
            'biometric': 'biometrics.csv',
            'serving': 'servings.csv',
            'note': 'notes.csv',
            'daily_summary': 'dailySummary.csv',
        }


    def load_exports_into_database(self):
        for export in self.export_types:
            export_filepath = self.export_directory / self.export_filenames[export]
            export_data = pd.read_csv(export_filepath)
            export_data['app_user_id'] = self.user.id

            """Rename the columns so that they match the model/table's column names"""
            column_names = export_data.columns.values.tolist()
            column_rename_map = {
                name: snake_case_cronometer_column_name(name)
                for name in column_names
            }
            export_data = export_data.rename(columns=column_rename_map)

            export_data.to_sql(
                name=self.export_models[export].__table__.name,
                con=self.session.get_bind(),
                if_exists='append',
                index=False,
            )
