import time
from multiprocessing import Queue
from threading import Thread

from historian.loader import fetch_historical_data
from historian.loader.job import Job
from historian.storage import insert_mt5_ticks, insert_mt5_rates, update_job_status
from loguru import logger


class ImportManager:

    def __init__(self):
        self.queue = Queue()
        thread = Thread(target=self.process)
        thread.daemon = True
        thread.start()

    def add_job(self, job: Job):
        self.queue.put_nowait(job)

    def process(self):
        queue = self.queue
        while True:
            if not queue.empty():
                job = queue.get()
                ImportManager.__process_job__(job)
            else:
                time.sleep(5)

    @staticmethod
    def __process_job__(job: Job):
        try:
            ImportManager.__insert_data__(job)
            update_job_status(job.id, "COMPLETED")
        except Exception as e:
            print(e)
            update_job_status(job.id, "ERROR")

    @staticmethod
    def __insert_data__(job):
        logger.info("Fetch data for {} {} {} - {}", job.instrument_id, job.instrument_type, job.start_time,
                    job.end_time)
        data = fetch_historical_data(
            job.instrument_id,
            job.instrument_type,
            job.start_time,
            job.end_time
        )
        if len(data) > 0:
            if job.instrument_type == "tick":
                insert_mt5_ticks(data)
            else:
                insert_mt5_rates(data)
