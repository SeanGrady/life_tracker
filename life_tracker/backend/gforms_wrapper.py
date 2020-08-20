import argparse
import gspread
from .models import (
    MoodSurveyResponse,
    SleepSurveyResponse,
    AppUser,
)
from dateutil.parser import parse
from .crud import (
    insert_if_not_exists,
    contextual_session,
)


survey_types = {
    'mood': "Daily Mood Survey (Responses)",
    'sleep': "Daily Sleep Survey (Responses)",
}

def download_gforms_data(session, user):

    user_email = user.email
    gspread_client = gspread.oauth()

    for survey_type, spreadsheet_name in survey_types.items():
        response_spreadsheet = gspread_client.open(spreadsheet_name)
        response_worksheet = response_spreadsheet.get_worksheet(0)
        unfiltered_survey_responses = response_worksheet.get_all_records()
        user_survey_responses = [
            response for response in unfiltered_survey_responses
            if response['Email Address'] == user.email
        ]
        add_survey_responses_to_database(session, user, survey_type, user_survey_responses)


def add_survey_responses_to_database(session, user, survey_type, survey_responses):
    user_id = user.id
    rows = []
    if survey_type == 'mood':
        model = MoodSurveyResponse
        for survey_response in survey_responses:
            row = {
                "mood": survey_response['Mood'],
                "energy": survey_response['Energy'],
                "sleep_hours": survey_response['Sleep Hours'],
                "adderall_crash": survey_response['Adderall Crash'],
                "date_time": parse(survey_response['Timestamp']),
                "app_user_id": user_id,
            }
            rows.append(row)
    elif survey_type == 'sleep':
        model = SleepSurveyResponse
        for survey_response in survey_responses:
            row = {
                "sleep_quality": survey_response['Quality'],
                "sleep_hours": survey_response['Hours'],
                "rise_ease": survey_response['Rise'],
                "date_time": parse(survey_response['Timestamp']),
                "app_user_id": user_id,
            }
            rows.append(row)

    insert_if_not_exists(session, model, rows)

def download_gforms_responses_for_user(user_id):
    with contextual_session() as session:
        user = session.query(AppUser).get(user_id)
        download_gforms_data(session, user)
