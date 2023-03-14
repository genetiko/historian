"""Create instruments table

Revision ID: 7acc051d3b05
Revises: e73b59bd1ecb
Create Date: 2023-03-14 16:23:54.330711

"""
from alembic import op
from sqlalchemy import Column, SmallInteger, ForeignKey, String, Float, Boolean, UniqueConstraint

# revision identifiers, used by Alembic.
revision = '7acc051d3b05'
down_revision = 'e73b59bd1ecb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'instruments',
        Column('id', SmallInteger, primary_key=True),
        Column('source_id', SmallInteger, ForeignKey('sources.id'), nullable=False),
        Column('name', String(256), nullable=False),
        Column('path', String(256), nullable=False),
        Column('currency_base', String(32), nullable=False),
        Column('currency_margin', String(32), nullable=False),
        Column('currency_profit', String(32), nullable=False),
        Column('description', String(256), nullable=False),
        Column('digits', SmallInteger, nullable=False),
        Column('volume_min', Float, nullable=False),
        Column('volume_max', Float, nullable=False),
        Column('volume_step', Float, nullable=False),
        Column('spread_floating', Boolean, nullable=False),
        UniqueConstraint('source_id', 'name', name='instrument')
    )


def downgrade() -> None:
    op.drop_table('instruments')
