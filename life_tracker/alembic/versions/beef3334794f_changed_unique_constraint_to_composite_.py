"""changed unique constraint to composite PK

Revision ID: beef3334794f
Revises: bf3a905413ee
Create Date: 2020-07-08 17:00:32.784236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beef3334794f'
down_revision = 'bf3a905413ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('mood_survey_response_app_user_id_date_time_key', 'mood_survey_response', type_='unique')
    op.drop_column('mood_survey_response', 'id')
    # ### end Alembic commands ###
    op.create_primary_key(
        'pk_mood_survey_response',
        'mood_survey_response',
        ['date_time', 'app_user_id'],
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mood_survey_response', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.create_unique_constraint('mood_survey_response_app_user_id_date_time_key', 'mood_survey_response', ['app_user_id', 'date_time'])
    # ### end Alembic commands ###
