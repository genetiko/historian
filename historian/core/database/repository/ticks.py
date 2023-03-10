from sqlalchemy.orm import Session

from historian.core.database.config import Session


def insert_ticks(ticks):
    with Session() as session:
        session.bulk_save_objects(ticks)
        session.commit()
