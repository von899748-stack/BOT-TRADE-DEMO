from __future__ import annotations


def pair_risk_multiplier(symbol: str) -> float:
    high_vol = {"BTC/USD", "ETH/USD", "USD/TRY", "USD/RUB", "USD/ZAR", "USD/BRL"}
    return 0.5 if symbol in high_vol else 1.0
