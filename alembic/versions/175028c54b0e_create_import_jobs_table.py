"""Create import_jobs table

Revision ID: 175028c54b0e
Revises: 7bd4f4fd49c6
Create Date: 2023-03-14 16:24:20.701224

"""
from alembic import op
from sqlalchemy import Integer, Column, String, DateTime, ForeignKey

from historian import settings

# revision identifiers, used by Alembic.
revision = '175028c54b0e'
down_revision = '7bd4f4fd49c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'import_jobs',
        Column('id', Integer, primary_key=True),
        Column('instrument_id', Integer, ForeignKey('historian.instruments.id'), nullable=False),
        Column('timeframe', String(16), nullable=False),
        Column('from_date', DateTime, nullable=False),
        Column('to_date', DateTime, nullable=False),
        Column('status', String(64), nullable=False),
        schema=settings.db.schema
    )


def downgrade() -> None:
    op.drop_table('import_jobs')
