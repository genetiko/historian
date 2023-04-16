import pandas as pd
from sqlalchemy.dialects.postgresql import insert

from historian import SessionMaker
from .models import Instrument, Source, Rate, Tick, ImportJob, ImportJobChunk
from ..loader import fetch_sources, fetch_instruments


def insert_mt5_rates(rates):
    with SessionMaker() as session:
        session.bulk_save_objects(rates)
        session.commit()


def insert_sources(sources):
    with SessionMaker() as session:
        session.execute(insert(Source)
                        .values(sources)
                        .on_conflict_do_nothing())
        session.commit()


def insert_instruments(instruments):
    with SessionMaker() as session:
        session.execute(insert(Instrument)
                        .values(instruments)
                        .on_conflict_do_nothing())
        session.commit()


def insert_mt5_ticks(ticks):
    with SessionMaker() as session:
        session.bulk_save_objects(ticks)
        session.commit()


def get_mt5_rates(instrument, start_time, end_time):
    with SessionMaker() as session:
        return session.query(Rate) \
            .where(Rate.instrument_id == instrument) \
            .where(Rate.timestamp.between(start_time, end_time)) \
            .order_by(Rate.timestamp)


def get_mt5_ticks(instrument, start_time, end_time):
    with SessionMaker() as session:
        return session.query(Tick) \
            .where(Tick.instrument_id == instrument) \
            .where(Tick.timestamp.between(start_time, end_time)) \
            .order_by(Tick.timestamp)


def get_all_sources(force_update):
    with SessionMaker() as session:
        if force_update:
            insert_sources(fetch_sources())
        return session.query(Source).all()


def get_all_instruments(source_id, force_update):
    with SessionMaker() as session:
        if force_update:
            insert_instruments(fetch_instruments(source_id))
        return session.query(Instrument).where(source_id == source_id).all()


def insert_job(instrument_id, instrument_type, start_time, end_time, chunks):
    import_job_chunks = [ImportJobChunk(start_time=rp[0], end_time=rp[1], status="CREATED") for rp in chunks]

    job = ImportJob(
        instrument_id=instrument_id,
        chunks=import_job_chunks,
        timeframe=instrument_type,
        start_time=start_time,
        end_time=end_time,
        status="CREATED"
    )

    with SessionMaker() as session:
        session.add(job)
        session.commit()
        return session.get(ImportJob, job.id)
