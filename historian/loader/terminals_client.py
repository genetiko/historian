import struct

import httpx

from historian import settings


def fetch_import_chunks(instrument_id, instrument_type, start_time, end_time):
    params = {
        "instrument_id": instrument_id,
        "instrument_type": instrument_type,
        "start_time": start_time,
        "end_time": end_time
    }
    with httpx.Client(base_url=settings.terminals.baseUrl) as client:
        res = client.get("/chunks", params=params)
        return res.json()


def fetch_historical_data(instrument_id, instrument_type, start_time, end_time):
    if instrument_type == "tick":
        pack_string = '<Qffif'
    else:
        pack_string = '<QffffiiB'
    struct_size = struct.calcsize(pack_string)

    params = {
        "instrument_type": instrument_type,
        "start_time": start_time,
        "end_time": end_time
    }

    with httpx.Client(base_url=settings.terminals.baseUrl, timeout=300) as client:
        with client.stream("GET", f"/data/{instrument_id}", params=params) as stream:
            return [struct.unpack_from(pack_string, buffer, 0) for buffer in stream.iter_bytes(chunk_size=struct_size)]


def fetch_sources():
    with httpx.Client(base_url=settings.terminals.baseUrl) as client:
        res = client.get("/sources")
        return res.json()


def fetch_instruments(terminal_id):
    with httpx.Client(base_url=settings.terminals.baseUrl) as client:
        res = client.get(f"/instruments/{terminal_id}")
        return res.json()
