from fastapi import FastAPI

from historian.routers import history
from historian.routers import symbols

app = FastAPI()

app.include_router(symbols.router)
app.include_router(history.router)
