from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass(slots=True)
class HistoricalDataConfig:
    """Configuration for historical market data download/backfill."""

    symbols: list[str] = field(default_factory=list)
    start_date: date = date(2010, 1, 1)
    end_date: date = field(default_factory=date.today)
    timeframe: str = "1D"
    output_dir: str = "data/historical"


@dataclass(slots=True)
class AppConfig:
    """Top-level application config."""

    app_name: str
    env: str
    historical_data: HistoricalDataConfig
