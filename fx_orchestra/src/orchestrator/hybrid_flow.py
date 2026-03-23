from __future__ import annotations

from importlib import import_module

_IMPORT_PREFIX = "src." if (__package__ or "").startswith("src.") else ""
build_technical_signal = import_module(
    f"{_IMPORT_PREFIX}agents.strategy.signal_fusion.technical_fusion"
).build_technical_signal
fetch_ohlcv = import_module(f"{_IMPORT_PREFIX}agents.tools.fetch_ohlcv").fetch_ohlcv
load_base_config = import_module(f"{_IMPORT_PREFIX}config.base").load_base_config


def run_hybrid_flow() -> list[dict]:
    cfg = load_base_config()
    out = []
    for symbol in cfg.historical_data.symbols:
        candles = fetch_ohlcv(symbol, cfg.historical_data.start_date, cfg.historical_data.end_date)
        out.append(build_technical_signal(symbol, candles))
    return out
