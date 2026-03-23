from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import argparse
from datetime import date

from agents.perception.technical.trend.sma import sma_signal
from data.sources.oanda_v20 import OandaV20Source


def backtest(symbol: str) -> dict:
    source = OandaV20Source()
    candles = source.fetch_ohlcv(symbol, date(2010, 1, 1), date.today())

    equity = 1.0
    signal = 0.0
    prev_close = float(candles[0]["close"])
    for idx, candle in enumerate(candles[1:], start=1):
        signal = sma_signal(candles[:idx])
        close = float(candle["close"])
        ret = (close - prev_close) / prev_close
        equity *= 1 + ret * signal
        prev_close = close

    return {"symbol": symbol, "signal": signal, "final_equity": equity}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", help="e.g. USD/TRY")
    args = parser.parse_args()
    print(backtest(args.symbol))


if __name__ == "__main__":
    main()
