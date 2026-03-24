"""Very small SMA-crossover backtest for one configured pair."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from config.base import build_default_config


def run_sma_backtest(
    data: pd.DataFrame,
    fast_window: int = 20,
    slow_window: int = 100,
) -> pd.DataFrame:
    """Build a simple strategy equity curve for a single instrument."""

    if "close" not in data.columns:
        raise ValueError("Input data must contain a 'close' column")

    frame = data.copy()
    frame["ret"] = frame["close"].pct_change().fillna(0.0)
    frame["fast"] = frame["close"].rolling(fast_window).mean()
    frame["slow"] = frame["close"].rolling(slow_window).mean()
    frame["signal"] = (frame["fast"] > frame["slow"]).astype(int)
    frame["position"] = frame["signal"].shift(1).fillna(0)
    frame["strategy_ret"] = frame["position"] * frame["ret"]
    frame["equity"] = (1 + frame["strategy_ret"]).cumprod()
    return frame


def main() -> None:
    cfg = build_default_config()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbol", default=cfg.benchmark_symbol)
    parser.add_argument("--data-dir", default=str(ROOT / cfg.data_dir))
    args = parser.parse_args()

    path = Path(args.data_dir) / f"{args.symbol.replace('/', '_')}.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"Data for {args.symbol} not found: {path}. "
            "Run scripts/download_historical.py first."
        )

    data = pd.read_csv(path)
    result = run_sma_backtest(data)

    total_return = result["equity"].iloc[-1] - 1
    max_drawdown = (result["equity"] / result["equity"].cummax() - 1).min()
    print(f"Backtest for {args.symbol}")
    print(f"Rows: {len(result)}")
    print(f"Total return: {total_return:.2%}")
    print(f"Max drawdown: {max_drawdown:.2%}")


if __name__ == "__main__":
    main()
