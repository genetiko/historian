"""create ticks table

Revision ID: 1e18d103822a
Revises: 
Create Date: 2023-03-05 21:46:30.289598

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '1e18d103822a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'ticks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('bid', sa.Float, nullable=False),
        sa.Column('ask', sa.Float, nullable=False),
        sa.Column('last', sa.Float, nullable=False),
        sa.Column('volume', sa.Integer, nullable=False),
        sa.Column('flags', sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('ticks')
