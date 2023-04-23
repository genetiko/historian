"""Create sources table

Revision ID: e73b59bd1ecb
Revises: 
Create Date: 2023-03-14 16:23:45.122839

"""
from alembic import op
from sqlalchemy import Column, SmallInteger, UniqueConstraint, String

from historian import settings

# revision identifiers, used by Alembic.
revision = 'e73b59bd1ecb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'sources',
        Column('id', SmallInteger, primary_key=True),
        Column('name', String(256), nullable=False),
        Column('server', String(256), nullable=False),
        UniqueConstraint('id', 'name', name='source'),
        schema=settings.db.schema
    )


def downgrade() -> None:
    op.drop_table('sources')
