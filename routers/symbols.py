from fastapi import APIRouter

router = APIRouter()


@router.get("/symbols", tags=["Symbols"])
async def get_symbols():
    return {"symbols": []}
