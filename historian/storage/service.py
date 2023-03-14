from sqlalchemy.orm import Session


def insert_mt5_rates(rates):
    with Session() as session:
        session.bulk_save_objects(rates)
        session.commit()


def insert_instruments(instruments):
    with Session() as session:
        session.bulk_save_objects(instruments)
        session.commit()


def insert_mt5_ticks(ticks):
    with Session() as session:
        session.bulk_save_objects(ticks)
        session.commit()
