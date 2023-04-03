import httpx

from historian import settings


def fetch_import_chunks(instrument_id, instrument_type, start_date, end_date):
    params = {
        "instrument_id": instrument_id,
        "instrument_type": instrument_type,
        "start_date": start_date,
        "end_date": end_date
    }
    with httpx.Client(base_url=settings.terminals.baseUrl) as client:
        r = client.get("/chunks", params=params)
        return r.json()


def fetch_historical_data(instrument_id, instrument_type_id, date):
    pass


def fetch_sources():
    with httpx.Client(base_url=settings.terminals.baseUrl) as client:
        r = client.get("/sources")
        return r.json()


def fetch_instruments(terminal_id):
    with httpx.Client(base_url=settings.terminals.baseUrl) as client:
        r = client.get("/instruments", params={"terminal_id": terminal_id})
        return r.json()
