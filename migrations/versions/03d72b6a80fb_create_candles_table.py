"""Create candles table

Revision ID: 03d72b6a80fb
Revises: 1e18d103822a
Create Date: 2023-03-06 12:50:28.542769

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '03d72b6a80fb'
down_revision = '1e18d103822a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'candles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('timestamp', sa.Integer),
        sa.Column('open', sa.Float),
        sa.Column('high', sa.Float),
        sa.Column('low', sa.Float),
        sa.Column('close', sa.Float),
        sa.Column('tick_volume', sa.Integer),
        sa.Column('volume', sa.Integer),
        sa.Column('spread', sa.Integer),
    )


def downgrade() -> None:
    op.drop_table('candles')
