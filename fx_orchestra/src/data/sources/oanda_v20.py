from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
import random


@dataclass(slots=True)
class OandaV20Source:
    """Offline-friendly OHLCV generator that mimics broker candles."""

    seed: int = 7

    def fetch_ohlcv(self, symbol: str, start: date, end: date, timeframe: str = "1D") -> list[dict]:
        if timeframe != "1D":
            raise ValueError("This scaffold currently supports only 1D candles")

        if end < start:
            return []

        rng = random.Random(f"{symbol}-{self.seed}")
        current = start
        price = self._base_price(symbol)
        candles: list[dict] = []

        while current <= end:
            ret = rng.gauss(0.0001, 0.01)
            open_ = price
            close = max(1e-8, open_ * (1 + ret))
            spread = max(abs(rng.gauss(0.001, 0.0005)), 0.0002)
            high = max(open_, close) * (1 + spread)
            low = min(open_, close) * (1 - spread)
            volume = rng.randint(1200, 24000)
            candles.append(
                {
                    "timestamp": current.isoformat(),
                    "open": round(open_, 6),
                    "high": round(high, 6),
                    "low": round(low, 6),
                    "close": round(close, 6),
                    "volume": volume,
                    "symbol": symbol,
                }
            )
            price = close
            current += timedelta(days=1)

        return candles

    @staticmethod
    def _base_price(symbol: str) -> float:
        defaults = {
            "USD/TRY": 1.5,
            "USD/ZAR": 7.3,
            "USD/BRL": 1.8,
            "USD/MXN": 12.5,
            "USD/INR": 46.0,
            "USD/CNH": 6.8,
            "USD/HKD": 7.75,
            "USD/SGD": 1.35,
            "USD/RUB": 30.0,
            "USD/NOK": 6.0,
            "USD/SEK": 7.0,
            "USD/DKK": 5.3,
            "USD/CZK": 18.0,
            "USD/HUF": 190.0,
            "USD/PLN": 3.0,
            "BTC/USD": 0.3,
            "ETH/USD": 0.1,
        }
        return defaults.get(symbol, 1.0)
