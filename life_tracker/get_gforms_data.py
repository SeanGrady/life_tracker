import gspread
from models import MoodSurveyResponse
from dateutil.parser import parse
from crud import scoped_session


# config
user_id = 1


def get_survey_responses():
    spreadsheet_name = "Daily Mood Survey (Responses)"
    gspread_client = gspread.oauth()

    response_spreadsheet = gspread_client.open(spreadsheet_name)
    response_worksheet = response_spreadsheet.get_worksheet(0)
    survey_responses = response_worksheet.get_all_records()
    return survey_responses


def add_responses_to_database(survey_responses):
    survey_records = []
    for survey_response in survey_responses:
        response_record = MoodSurveyResponse(
            mood=survey_response['Mood'],
            energy=survey_response['Energy'],
            sleep_hours=survey_response['Sleep Hours'],
            adderall_crash=survey_response['Adderall Crash'],
            date_time=parse(survey_response['Timestamp']),
            app_user_id=user_id,
        )
        survey_records.append(response_record)
    with scoped_session() as session:
        session.query(MoodSurveyResponse).filter_by(app_user_id=user_id).all()
        for survey_record in survey_records:
            session.merge(survey_record)

if __name__ == '__main__':
    survey_responses = get_survey_responses()
    add_responses_to_database(survey_responses)
