from historian import SessionMaker

from .models import Instrument, Source, Rate, Tick


def insert_mt5_rates(rates):
    with SessionMaker() as session:
        session.bulk_save_objects(rates)
        session.commit()


def insert_instruments(instruments):
    with SessionMaker() as session:
        session.bulk_save_objects(instruments)
        session.commit()


def insert_mt5_ticks(ticks):
    with SessionMaker() as session:
        session.bulk_save_objects(ticks)
        session.commit()


def get_mt5_rates(instrument, from_date, to_date):
    with SessionMaker() as session:
        return session.query(Rate) \
            .where(Rate.instrument_id == instrument) \
            .where(Rate.timestamp.between(from_date, to_date)) \
            .order_by(Rate.timestamp)


def get_mt5_ticks(instrument, from_date, to_date):
    with SessionMaker() as session:
        return session.query(Tick) \
            .where(Tick.instrument_id == instrument) \
            .where(Tick.timestamp.between(from_date, to_date)) \
            .order_by(Tick.timestamp)


def get_all_sources():
    with SessionMaker() as session:
        return session.query(Source).all()


def get_all_instruments():
    with SessionMaker() as session:
        return session.query(Instrument).all()
