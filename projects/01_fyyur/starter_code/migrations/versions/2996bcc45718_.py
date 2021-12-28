"""empty message

Revision ID: 2996bcc45718
Revises: 983ecf9c3e7c
Create Date: 2021-12-28 19:34:19.130077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2996bcc45718'
down_revision = '983ecf9c3e7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###