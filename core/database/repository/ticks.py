from sqlalchemy.orm import Session

from core.database.config import Session


def insert_ticks(ticks):
    with Session() as session:
        session.bulk_save_objects(ticks)
        session.commit()
