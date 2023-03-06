from dotenv import load_dotenv
from fastapi import FastAPI

from routers import symbols, history

load_dotenv()

app = FastAPI()

app.include_router(symbols.router)
app.include_router(history.router)
