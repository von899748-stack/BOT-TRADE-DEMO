"""Download historical OHLCV for configured FX + crypto instruments."""

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


def download_one(ticker: str, start: str, end: str, interval: str) -> pd.DataFrame:
    """Download data with yfinance and normalize output columns."""

    try:
        import yfinance as yf
    except ImportError as exc:  # pragma: no cover - runtime dependency only
        raise RuntimeError(
            "yfinance is required. Install with: pip install yfinance"
        ) from exc

    frame = yf.download(
        tickers=ticker,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=False,
        progress=False,
        threads=False,
    )
    if frame.empty:
        return frame

    frame = frame.rename_axis("timestamp").reset_index()
    frame.columns = [str(c).lower().replace(" ", "_") for c in frame.columns]
    return frame


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default=None,
        help="Override output folder (default comes from config)",
    )
    args = parser.parse_args()

    cfg = build_default_config()
    out_dir = Path(args.out or (ROOT / cfg.data_dir))
    out_dir.mkdir(parents=True, exist_ok=True)

    start = cfg.history.start.isoformat()
    end = cfg.history.end.isoformat()

    for instrument in cfg.instruments:
        frame = download_one(
            ticker=instrument.provider_symbol,
            start=start,
            end=end,
            interval=cfg.timeframe,
        )
        output_file = out_dir / f"{instrument.symbol.replace('/', '_')}.csv"
        if frame.empty:
            print(f"[WARN] no data for {instrument.symbol} ({instrument.provider_symbol})")
            continue

        frame["symbol"] = instrument.symbol
        frame.to_csv(output_file, index=False)
        print(f"[OK] saved {instrument.symbol}: {len(frame)} rows -> {output_file}")


if __name__ == "__main__":
    main()
