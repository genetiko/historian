from datetime import datetime
from typing import List

from fastapi import APIRouter, Response, status

from historian.storage import Tick, Rate, insert_mt5_ticks, insert_mt5_rates, get_mt5_rates, get_mt5_ticks, insert_job
from .models import RateModel, TickModel

router = APIRouter()


@router.get("/history/{instrument_id}/rates", tags=["History"], response_model=List[RateModel])
async def get_rates_history(instrument_id, from_date: datetime, to_date: datetime):
    return list(get_mt5_rates(instrument_id, from_date, to_date))


@router.get("/history/{instrument_id}/ticks", tags=["History"], response_model=List[TickModel])
async def get_ticks_history(instrument_id, from_date: datetime, to_date: datetime):
    return list(get_mt5_ticks(instrument_id, from_date, to_date))


@router.post("/history/{instrument_id}/prepare", tags=["History"])
async def prepare_data(instrument_id: int, timeframe: str, from_date: datetime, to_date: datetime):
    insert_job(instrument_id, timeframe, from_date, to_date)
    return Response(status_code=status.HTTP_200_OK)


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
