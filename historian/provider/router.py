from fastapi import APIRouter

from historian.storage import get_all_instruments
from historian.storage import get_all_sources

router = APIRouter()


@router.get("/instruments/{source_id}", tags=["Metadata"])
async def get_instruments(source_id: str, force_update: bool = False):
    return {"instruments": get_all_instruments(source_id, force_update)}


@router.get("/sources", tags=["Metadata"])
async def get_sources(force_update: bool = False):
    return {"sources": get_all_sources(force_update)}
