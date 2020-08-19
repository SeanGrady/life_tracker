from dash.dependencies import (
    Input,
    Output,
)
from flask_login import current_user
from flask import current_app as app
from dash.dependencies import (
    Input,
    Output,
)
import pandas as pd
from plotly import (
    express as px,
    graph_objects as go,
)
from ...backend.models import(
    AppUser,
    MoodSurveyResponse,
    SleepSurveyResponse,
)


metric_checklist_kwargs = {
    'options': [
        {'label': 'Daily Mood (1-5)', 'value': 'DMD'},
        {'label': 'Sleep Hours', 'value': 'HRS'},
        {'label': 'Sleep Quality (1-5)', 'value': 'QLT'},
        {'label': 'Rise Ease (1-5)', 'value': 'EAS'},
        {'label': 'Adderal Crash (0-3)', 'value': 'CRS'},
        {'label': 'Energy (1-5)', 'value': 'ENR'},
    ],
    'value': [
        'DMD',
        'HRS',
    ],
    'labelStyle': {
        'display': 'inline-block',
    }
}

metric_column_map = {
    'HRS': 'sleep_hours',
    'QLT': 'sleep_quality',
    'EAS': 'rise_ease',
    'DMD': 'mood',
    'CRS': 'adderall_crash',
    'ENR': 'energy',
}


def register_callbacks(dash_app):
    @dash_app.callback(Output('metric-graph', 'figure'), [Input('metric-checklist', 'value')])
    def update_graph(metrics):
        if current_user.is_authenticated:
            mood_survey_data = pd.read_sql(
                app.session.query(
                    MoodSurveyResponse.mood,
                    MoodSurveyResponse.adderall_crash,
                    MoodSurveyResponse.energy,
                    MoodSurveyResponse.date_time,
                ).filter(
                    MoodSurveyResponse.app_user == current_user
                ).statement,
                app.session.bind,
            )
            sleep_survey_data = pd.read_sql(
                app.session.query(
                    SleepSurveyResponse.sleep_hours,
                    SleepSurveyResponse.date_time,
                    SleepSurveyResponse.sleep_quality,
                    SleepSurveyResponse.rise_ease,
                ).filter(
                    SleepSurveyResponse.app_user == current_user
                ).statement,
                app.session.bind
            )
            mood_survey_data.set_index('date_time')
            sleep_survey_data.set_index('date_time')
            combined_data = pd.merge(sleep_survey_data, mood_survey_data, how='outer')
            # import pdb;pdb.set_trace()
            fig = go.Figure()
            for metric in metrics:
                column_name = metric_column_map[metric]
                fig.add_trace(
                    go.Scatter(
                        x=combined_data['date_time'],
                        y=combined_data[column_name],
                        mode='lines',
                        name=column_name,
                    )
                )
            return fig
        else:
            return {
                "layout": {
                    "xaxis": {
                        "visible": false
                    },
                    "yaxis": {
                        "visible": false
                    },
                    "annotations": [
                        {
                            "text": "No matching data found",
                            "xref": "paper",
                            "yref": "paper",
                            "showarrow": false,
                            "font": {
                                "size": 28
                            }
                        }
                    ]
                }
            }
