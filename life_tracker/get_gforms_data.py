import argparse
import gspread
from models import (
    MoodSurveyResponse,
    SleepSurveyResponse,
    AppUser,
)
from dateutil.parser import parse
from crud import (
    insert_if_not_exists,
    scoped_session,
)


# config
user_id = 1


def insert_survey_responses(survey_type):
    if survey_type == 'mood':
        spreadsheet_name = "Daily Mood Survey (Responses)"
    elif survey_type == 'sleep':
        spreadsheet_name = "Daily Sleep Survey (Responses)"

    gspread_client = gspread.oauth()

    response_spreadsheet = gspread_client.open(spreadsheet_name)
    response_worksheet = response_spreadsheet.get_worksheet(0)
    survey_responses = response_worksheet.get_all_records()
    add_survey_responses_to_database(survey_type, survey_responses)


def add_survey_responses_to_database(survey_type, survey_responses):
    with scoped_session() as session:
        try:
            user = session.query(AppUser).filter_by(id=user_id).one()
        except:
            import pdb;pdb.set_trace()
            raise ValueError("Invalid user ID")
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--filetype',
        help="Survey type. 'mood' for mood survey, 'sleep' for sleep survey",
        type=str,
    )
    args = parser.parse_args()
    survey_type = args.filetype
    insert_survey_responses(survey_type)
