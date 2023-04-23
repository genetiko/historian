from sqlalchemy import update, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import joinedload

from historian import SessionMaker
from .models import Instrument, Source, Rate, Tick, ImportJob, ImportJobChunk
from ..loader import fetch_sources, fetch_instruments


def insert_mt5_rates(rates):
    with SessionMaker() as session:
        insert_stmt = insert(Rate).values(rates)
        update_stmt = insert_stmt.on_conflict_do_update(
            constraint="uc_mt5_rate",
            set_={
                "open": insert_stmt.excluded.open,
                "high": insert_stmt.excluded.high,
                "low": insert_stmt.excluded.low,
                "close": insert_stmt.excluded.close,
                "volume": insert_stmt.excluded.volume,
                "spread": insert_stmt.excluded.spread,
            }
        )
        session.execute(update_stmt)
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
        session.execute(insert(Tick)
                        .values(ticks)
                        .on_conflict_do_nothing())
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


def get_all_jobs():
    with SessionMaker() as session:
        return session.query(ImportJob).all()


def get_all_instruments(source_id, force_update):
    with SessionMaker() as session:
        if force_update:
            insert_instruments(fetch_instruments(source_id))
        return session.query(Instrument).where(Instrument.source_id == source_id).all()


def insert_job(instrument_id, instrument_type, start_time, end_time, chunks):
    import_job_chunks = [ImportJobChunk(start_time=rp[0], end_time=rp[1], status="CREATED") for rp in chunks]

    job = ImportJob(
        instrument_id=instrument_id,
        chunks=import_job_chunks,
        instrument_type=instrument_type,
        start_time=start_time,
        end_time=end_time,
        status="CREATED"
    )

    with SessionMaker() as session:
        session.add(job)
        session.commit()
        return session.get(ImportJob, job.id)


def update_job_status(job_id, status):
    with SessionMaker() as session:
        session.execute(update(ImportJobChunk).where(ImportJobChunk.id == job_id).values({"status": status}))
        session.commit()


def get_uncompleted_jobs():
    with SessionMaker() as session:
        return session.query(ImportJob) \
            .join(ImportJob.chunks) \
            .filter(ImportJobChunk.status.in_(["CREATED", "ERROR"])) \
            .all()

# with sub as (select job.import_job_id as id,
#                     count(*)          as cnt
#              from import_job_chunks job
#              group by job.import_job_id)
# select job.id,
#        chunk.status,
#        round(count(*) / (select sum(cnt) from sub where sub.id = job.id) * 100, 2) as percent
# from import_jobs job
#          inner join import_job_chunks chunk on job.id = chunk.import_job_id
# group by job.id, chunk.status;

# def get_jobs_progress():
#     with SessionMaker() as session:
#         session.query(
#             ImportJobChunk,
#             sqlalchemy.over(func.count()),
#         )
