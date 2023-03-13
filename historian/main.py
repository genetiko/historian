from fastapi import FastAPI
from fastapi.responses import JSONResponse

from historian.loader.router import router as loader_router
from historian.provider.router import router as provider_router

app = FastAPI()


@app.get('/')
async def main():
    return JSONResponse(content={})


app.include_router(provider_router)
app.include_router(loader_router)
