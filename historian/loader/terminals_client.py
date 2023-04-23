import datetime
import struct

import httpx

from historian import settings


def fetch_import_chunks(instrument_id, instrument_type, start_time, end_time, frequency):
    params = {
        "instrument_id": instrument_id,
        "instrument_type": instrument_type,
        "start_time": start_time,
        "end_time": end_time,
        "frequency": frequency
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

    def map_value(value):
        if instrument_type == "tick":
            (timestamp, bid, ask, volume, flags) = value
            return {
                "instrument_id": instrument_id,
                "timestamp": datetime.datetime.fromtimestamp(timestamp),
                "bid": bid,
                "ask": ask,
                # "volume": volume,
                # "flags": flags,
            }
        else:
            (timestamp, open, high, low, close, tick_volume, volume, spread) = value
            return {
                "instrument_id": instrument_id,
                "timestamp": datetime.datetime.fromtimestamp(timestamp),
                "instrument_type": instrument_type,
                "open": open,
                "high": high,
                "low": low,
                "close": close,
                "volume": volume,
                "spread": spread,
            }

    with httpx.Client(base_url=settings.terminals.baseUrl, timeout=300) as client:
        with client.stream("GET", f"/data/{instrument_id}", params=params) as stream:
            return [map_value(struct.unpack_from(pack_string, buffer, 0)) for buffer in
                    stream.iter_bytes(chunk_size=struct_size)]


def fetch_sources():
    with httpx.Client(base_url=settings.terminals.baseUrl) as client:
        res = client.get("/sources")
        return res.json()


def fetch_instruments(terminal_id):
    with httpx.Client(base_url=settings.terminals.baseUrl) as client:
        res = client.get(f"/instruments/{terminal_id}")
        return res.json()
