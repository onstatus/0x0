"""add NSFW score

Revision ID: 7e246705da6a
Revises: 0cd36ecdd937
Create Date: 2017-10-27 03:07:48.179290

"""

# revision identifiers, used by Alembic.
revision = '7e246705da6a'
down_revision = '0cd36ecdd937'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('nsfw_score', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file', 'nsfw_score')
    # ### end Alembic commands ###
