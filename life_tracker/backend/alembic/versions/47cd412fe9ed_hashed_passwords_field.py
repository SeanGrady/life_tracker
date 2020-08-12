"""hashed passwords field

Revision ID: 47cd412fe9ed
Revises: 4dfcafa29296
Create Date: 2020-08-12 16:13:12.284836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47cd412fe9ed'
down_revision = '4dfcafa29296'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('app_user', sa.Column('password_hash', sa.String(), nullable=True))
    op.add_column('app_user', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('app_user', 'username')
    op.drop_column('app_user', 'password_hash')
    # ### end Alembic commands ###
