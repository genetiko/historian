from datetime import datetime
from typing import List

from fastapi import APIRouter, Response, status

from historian.storage import Tick, Rate, insert_mt5_ticks, insert_mt5_rates, get_mt5_rates, get_mt5_ticks, insert_job
from .models import RateModel, TickModel, ImportJobModel
from .terminals_client import fetch_import_chunks

router = APIRouter()


@router.get("/history/{instrument_id}/rates", tags=["History"], response_model=List[RateModel])
async def get_rates_history(instrument_id, start_time: datetime, end_time: datetime):
    return list(get_mt5_rates(instrument_id, start_time, end_time))


@router.get("/history/{instrument_id}/ticks", tags=["History"], response_model=List[TickModel])
async def get_ticks_history(instrument_id, start_time: datetime, end_time: datetime):
    return list(get_mt5_ticks(instrument_id, start_time, end_time))


@router.post("/history/{instrument_id}/prepare", tags=["History"], response_model=ImportJobModel)
async def prepare_data(instrument_id: int, instrument_type: str, start_time: datetime, end_time: datetime):
    chunks = fetch_import_chunks(instrument_id, instrument_type, start_time, end_time)
    return insert_job(instrument_id, instrument_type, start_time, end_time, chunks)


@router.post("/ticks", tags=["Test data endpoints"])
async def insert_ticks_data(ticks: List[TickModel]):
    data = [Tick(**t.dict()) for t in ticks]
    insert_mt5_ticks(data)
    return Response(status_code=status.HTTP_200_OK)


@router.post("/rates", tags=["Test data endpoints"])
async def insert_rates_data(rates: List[RateModel]):
    data = [Rate(**r.dict()) for r in rates]
    insert_mt5_rates(data)
    return Response(status_code=status.HTTP_200_OK)
