from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from config.base import load_base_config
from data.sources.oanda_v20 import OandaV20Source
from data.storage.timescaledb import TimescaleDBStorage


def main() -> None:
    cfg = load_base_config()
    source = OandaV20Source()
    storage = TimescaleDBStorage(output_dir=cfg.historical_data.output_dir)

    print(
        f"Downloading {len(cfg.historical_data.symbols)} symbols "
        f"from {cfg.historical_data.start_date} to {cfg.historical_data.end_date}"
    )

    for symbol in cfg.historical_data.symbols:
        frame = source.fetch_ohlcv(symbol, cfg.historical_data.start_date, cfg.historical_data.end_date)
        out = storage.write_ohlcv(symbol, frame)
        print(f"Saved {symbol:<8} -> {out}")


if __name__ == "__main__":
    main()
