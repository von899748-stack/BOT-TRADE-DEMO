from __future__ import annotations

from agents.strategy.signal_fusion.technical_fusion import build_technical_signal
from agents.tools.fetch_ohlcv import fetch_ohlcv
from config.base import load_base_config


def run_hybrid_flow() -> list[dict]:
    cfg = load_base_config()
    out = []
    for symbol in cfg.historical_data.symbols:
        candles = fetch_ohlcv(symbol, cfg.historical_data.start_date, cfg.historical_data.end_date)
        out.append(build_technical_signal(symbol, candles))
    return out
