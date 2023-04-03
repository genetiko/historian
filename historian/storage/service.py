import pandas as pd

from historian import SessionMaker
from .models import Instrument, Source, Rate, Tick, ImportJob, ImportJobChunk


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


def insert_job(instrument_id, timeframe, from_date, to_date):
    ranges = pd.Series(pd.date_range(from_date, to_date, freq="1000T"))
    range_pairs = list(zip(ranges[0::1], ranges[1::1]))

    chunks = [ImportJobChunk(from_date=rp[0], to_date=rp[1], status="CREATED") for rp in range_pairs]

    job = ImportJob(
        instrument_id=instrument_id,
        chunks=chunks,
        timeframe=timeframe,
        from_date=from_date,
        to_date=to_date,
        status="CREATED"
    )

    with SessionMaker() as session:
        session.add(job)
        session.commit()
