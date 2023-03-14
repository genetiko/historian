from fastapi import APIRouter

router = APIRouter()


@router.get("/instruments", tags=["Instruments"])
async def get_instruments():
    return {"instruments": []}
