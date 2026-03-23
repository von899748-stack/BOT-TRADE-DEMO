from __future__ import annotations


def atr(candles: list[dict], period: int = 14) -> float:
    if len(candles) < period + 1:
        return 0.0

    true_ranges: list[float] = []
    prev_close = float(candles[0]["close"])
    for candle in candles[1:]:
        high = float(candle["high"])
        low = float(candle["low"])
        close = float(candle["close"])
        tr = max(high - low, abs(high - prev_close), abs(low - prev_close))
        true_ranges.append(tr)
        prev_close = close

    recent = true_ranges[-period:]
    return sum(recent) / len(recent)
