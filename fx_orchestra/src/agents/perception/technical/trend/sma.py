from __future__ import annotations


def _rolling_mean(values: list[float], window: int) -> float | None:
    if len(values) < window or window <= 0:
        return None
    subset = values[-window:]
    return sum(subset) / window


def sma_signal(candles: list[dict], fast: int = 20, slow: int = 50) -> float:
    """Return signal in [-1, 1] based on fast/slow SMA spread."""

    closes = [float(c["close"]) for c in candles]
    fast_ma = _rolling_mean(closes, fast)
    slow_ma = _rolling_mean(closes, slow)
    if fast_ma is None or slow_ma is None:
        return 0.0
    spread = (fast_ma - slow_ma) / max(abs(slow_ma), 1e-8)
    return float(max(min(spread * 8, 1.0), -1.0))
