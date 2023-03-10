from sqlalchemy.orm import Session


def insert_candles(candles):
    with Session() as session:
        session.bulk_save_objects(candles)
        session.commit()


def insert_symbols(symbols):
    with Session() as session:
        session.bulk_save_objects(symbols)
        session.commit()


def insert_ticks(ticks):
    with Session() as session:
        session.bulk_save_objects(ticks)
        session.commit()
