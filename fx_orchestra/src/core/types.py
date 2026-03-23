from __future__ import annotations

from typing import Literal, TypedDict

Side = Literal["BUY", "SELL", "HOLD"]


class Signal(TypedDict):
    symbol: str
    side: Side
    score: float
