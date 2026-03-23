from __future__ import annotations

import csv
from pathlib import Path


class TimescaleDBStorage:
    """File-backed stand-in for TimescaleDB in local development."""

    def __init__(self, output_dir: str = "data/historical") -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write_ohlcv(self, symbol: str, candles: list[dict]) -> Path:
        out = self.output_dir / f"{symbol.replace('/', '_')}.csv"
        with out.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["timestamp", "open", "high", "low", "close", "volume", "symbol"],
            )
            writer.writeheader()
            writer.writerows(candles)
        return out
