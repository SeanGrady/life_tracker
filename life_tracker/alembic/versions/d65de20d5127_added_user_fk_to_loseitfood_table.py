"""added user fk to loseitfood table

Revision ID: d65de20d5127
Revises: 6d893fd532d7
Create Date: 2020-07-08 16:03:26.104417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd65de20d5127'
down_revision = '6d893fd532d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('loseit_food', sa.Column('app_user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'loseit_food', 'app_user', ['app_user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'loseit_food', type_='foreignkey')
    op.drop_column('loseit_food', 'app_user_id')
    # ### end Alembic commands ###
