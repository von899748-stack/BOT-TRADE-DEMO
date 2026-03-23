from __future__ import annotations

from core.types import Signal
from agents.perception.technical.trend.sma import sma_signal


def build_technical_signal(symbol: str, frame) -> Signal:
    score = sma_signal(frame)
    if score > 0.1:
        side = "BUY"
    elif score < -0.1:
        side = "SELL"
    else:
        side = "HOLD"
    return {"symbol": symbol, "side": side, "score": float(score)}
