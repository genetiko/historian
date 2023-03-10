from sqlalchemy.orm import Session

from historian.core.database.config import Session


def insert_symbols(symbols):
    with Session() as session:
        session.bulk_save_objects(symbols)
        session.commit()
