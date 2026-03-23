"""Default application configuration for FX Orchestra."""

from __future__ import annotations

from datetime import date

from .schema import AppConfig, HistoricalRange, InstrumentSpec

_SUPPORTED_PAIRS: tuple[InstrumentSpec, ...] = (
    InstrumentSpec(symbol="USD/TRY", provider_symbol="TRY=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/ZAR", provider_symbol="ZAR=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/BRL", provider_symbol="BRL=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/MXN", provider_symbol="MXN=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/INR", provider_symbol="INR=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/CNH", provider_symbol="CNH=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/HKD", provider_symbol="HKD=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/SGD", provider_symbol="SGD=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/RUB", provider_symbol="RUB=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/NOK", provider_symbol="NOK=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/SEK", provider_symbol="SEK=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/DKK", provider_symbol="DKK=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/CZK", provider_symbol="CZK=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/HUF", provider_symbol="HUF=X", asset_class="fx"),
    InstrumentSpec(symbol="USD/PLN", provider_symbol="PLN=X", asset_class="fx"),
    InstrumentSpec(symbol="BTC/USD", provider_symbol="BTC-USD", asset_class="crypto"),
    InstrumentSpec(symbol="ETH/USD", provider_symbol="ETH-USD", asset_class="crypto"),
)


def build_default_config() -> AppConfig:
    """Return default config for requested cross pairs from 2010 to today."""

    return AppConfig(
        instruments=_SUPPORTED_PAIRS,
        history=HistoricalRange(start=date(2010, 1, 1), end=date.today()),
        timeframe="1d",
        data_dir="data/historical",
        benchmark_symbol="USD/TRY",
        metadata={
            "owner": "fx_orchestra",
            "strategy_mode": "multi-pair",
        },
    )
