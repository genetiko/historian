from sqlalchemy.orm import Session

from core.database.config import Session


def insert_candles(candles):
    with Session() as session:
        session.bulk_save_objects(candles)
        session.commit()
