"""Create import_job_chunks table

Revision ID: b867ab5b92ed
Revises: 175028c54b0e
Create Date: 2023-03-14 16:24:26.093481

"""
from alembic import op
from sqlalchemy import ForeignKey, Column, Integer, DateTime, String

from historian import settings

# revision identifiers, used by Alembic.
revision = 'b867ab5b92ed'
down_revision = '175028c54b0e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'import_job_chunks',
        Column('id', Integer, primary_key=True),
        Column('import_job_id', Integer, ForeignKey('historian.import_jobs.id'), nullable=False),
        Column('start_time', DateTime, nullable=False),
        Column('end_time', DateTime, nullable=False),
        Column('finish_date', DateTime),
        Column('status', String, nullable=False),
        schema=settings.db.schema
    )


def downgrade() -> None:
    op.drop_table('import_job_chunks')
