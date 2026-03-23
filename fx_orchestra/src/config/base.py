from __future__ import annotations

from .schema import AppConfig, HistoricalDataConfig

SUPPORTED_SYMBOLS = [
    "USD/TRY",
    "USD/ZAR",
    "USD/BRL",
    "USD/MXN",
    "USD/INR",
    "USD/CNH",
    "USD/HKD",
    "USD/SGD",
    "USD/RUB",
    "USD/NOK",
    "USD/SEK",
    "USD/DKK",
    "USD/CZK",
    "USD/HUF",
    "USD/PLN",
    "BTC/USD",
    "ETH/USD",
]


def load_base_config() -> AppConfig:
    """Return base config focused on EM FX + crypto majors from 2010 to now."""

    historical = HistoricalDataConfig(symbols=SUPPORTED_SYMBOLS)
    return AppConfig(app_name="fx_orchestra", env="dev", historical_data=historical)
