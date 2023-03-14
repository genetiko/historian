"""Create mt5_ticks table

Revision ID: cf0aabc1ae7c
Revises: 7acc051d3b05
Create Date: 2023-03-14 16:24:01.255536

"""
from alembic import op
from sqlalchemy import Float, Integer, BigInteger, Column, ForeignKey

# revision identifiers, used by Alembic.
revision = 'cf0aabc1ae7c'
down_revision = '7acc051d3b05'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'mt5_ticks',
        Column('id', Integer, primary_key=True),
        Column('instrument_id', Integer, ForeignKey("instruments.id"), nullable=False),
        Column('timestamp', BigInteger, nullable=False),
        Column('bid', Float),
        Column('ask', Float)
        # Column('last', Float, nullable=False),
        # Column('volume', Integer, nullable=False),
        # Column('flags', Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('mt5_ticks')
