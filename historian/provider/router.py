from fastapi import APIRouter

from historian.storage import get_all_instruments
from historian.storage import get_all_sources

router = APIRouter()


@router.get("/instruments", tags=["Metadata"])
async def get_instruments():
    return {"instruments": get_all_instruments()}


@router.get("/sources", tags=["Metadata"])
async def get_sources():
    return {"sources": get_all_sources()}
