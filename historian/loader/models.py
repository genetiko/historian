from datetime import datetime
from typing import List

from pydantic import BaseModel


class TickModel(BaseModel):
    id: int | None = None
    instrument_id: int
    bid: float
    ask: float
    timestamp: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class RateModel(BaseModel):
    id: int | None = None
    timestamp: datetime
    instrument_id: int
    period: int
    open: float
    high: float
    low: float
    close: float
    volume: int
    spread: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ImportJobModel(BaseModel):
    id: int
    chunks: List
    instrument_id: int
    instrument_type: str
    start_time: datetime
    end_time: datetime
    status: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
