from datetime import date

from config.base import build_default_config


def test_default_config_has_requested_pairs() -> None:
    cfg = build_default_config()
    symbols = {item.symbol for item in cfg.instruments}

    assert "USD/TRY" in symbols
    assert "USD/ZAR" in symbols
    assert "USD/BRL" in symbols
    assert "USD/MXN" in symbols
    assert "USD/INR" in symbols
    assert "USD/CNH" in symbols
    assert "USD/HKD" in symbols
    assert "USD/SGD" in symbols
    assert "USD/RUB" in symbols
    assert "USD/NOK" in symbols
    assert "USD/SEK" in symbols
    assert "USD/DKK" in symbols
    assert "USD/CZK" in symbols
    assert "USD/HUF" in symbols
    assert "USD/PLN" in symbols
    assert "BTC/USD" in symbols
    assert "ETH/USD" in symbols


def test_default_history_starts_2010() -> None:
    cfg = build_default_config()
    assert cfg.history.start == date(2010, 1, 1)
    assert cfg.history.end >= cfg.history.start
