from datetime import datetime

from fastapi import APIRouter

router = APIRouter()


@router.get("/history/{symbol}", tags=["History"])
async def get_history(symbol, from_date: datetime, to_date: datetime):
    return {
        "symbol": symbol,
        "from_date": from_date,
        "to_date": to_date
    }


@router.post("/history/{symbol}/prepare", tags=["History"])
async def prepare_data(symbol: str):
    return {
        "symbol": symbol
    }
