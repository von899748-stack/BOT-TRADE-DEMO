"""Typed schema for runtime configuration."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass(frozen=True, slots=True)
class HistoricalRange:
    """Inclusive date range used when pulling historical market data."""

    start: date
    end: date


@dataclass(frozen=True, slots=True)
class InstrumentSpec:
    """Metadata describing a tradeable instrument in the system."""

    symbol: str
    provider_symbol: str
    asset_class: str
    quote_currency: str = "USD"


@dataclass(frozen=True, slots=True)
class AppConfig:
    """Top-level config object used by scripts and orchestration."""

    instruments: tuple[InstrumentSpec, ...]
    history: HistoricalRange
    timeframe: str = "1d"
    data_dir: str = "data/historical"
    benchmark_symbol: str = "USD/TRY"
    metadata: dict[str, str] = field(default_factory=dict)
