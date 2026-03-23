from __future__ import annotations

from datetime import date

from data.sources.oanda_v20 import OandaV20Source


def fetch_ohlcv(symbol: str, start: date, end: date) -> list[dict]:
    source = OandaV20Source()
    return source.fetch_ohlcv(symbol=symbol, start=start, end=end)
