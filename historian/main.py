from fastapi import FastAPI
from fastapi.responses import JSONResponse

from historian.loader import submit_pending_jobs
from historian.loader import router as loader_router
from historian.provider import router as provider_router

app = FastAPI()
submit_pending_jobs()


@app.get('/')
async def main():
    return JSONResponse(content={})


app.include_router(provider_router)
app.include_router(loader_router)
