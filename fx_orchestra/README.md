# fx_orchestra

Scaffold for a modular multi-agent FX trading system.

## Market universe

Default config includes these instruments:

- USD/TRY
- USD/ZAR
- USD/BRL
- USD/MXN
- USD/INR
- USD/CNH
- USD/HKD
- USD/SGD
- USD/RUB
- USD/NOK
- USD/SEK
- USD/DKK
- USD/CZK
- USD/HUF
- USD/PLN
- BTC/USD
- ETH/USD

Historical download range defaults to **2010-01-01 through today**.

## Quick start

```bash
cd fx_orchestra
python -m pip install -e .
python -m pip install yfinance pandas
python scripts/download_historical.py
python scripts/backtest_single_pair.py --symbol USD/TRY
```
