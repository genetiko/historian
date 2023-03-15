"""Create mt5_rates table

Revision ID: 7bd4f4fd49c6
Revises: cf0aabc1ae7c
Create Date: 2023-03-14 16:24:05.709434

"""
from alembic import op
from sqlalchemy import Integer, Float, Column, SmallInteger, DateTime

# revision identifiers, used by Alembic.
revision = '7bd4f4fd49c6'
down_revision = 'cf0aabc1ae7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'mt5_rates',
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, nullable=False),
        Column('instrument_id', Integer, nullable=False),
        Column('period', SmallInteger, nullable=False),
        Column('open', Float, nullable=False),
        Column('high', Float, nullable=False),
        Column('low', Float, nullable=False),
        Column('close', Float, nullable=False),
        Column('volume', Integer, nullable=False),
        Column('spread', Integer, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('mt5_rates')
