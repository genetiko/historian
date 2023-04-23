from historian.loader import ImportManager, Job
from historian.storage import get_uncompleted_jobs
from loguru import logger

manager = ImportManager()


def submit_pending_jobs():
    jobs = get_uncompleted_jobs()
    for job in jobs:
        submit_job(job)


def submit_job(job):
    logger.info("Submit {} chunks", len(job.chunks))
    for chunk in job.chunks:
        manager.add_job(Job(chunk.id, job.instrument_id, job.instrument_type, chunk.start_time, chunk.end_time))
