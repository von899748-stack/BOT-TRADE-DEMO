# fx_orchestra

Modular scaffold for a multi-agent trading workflow focused on:

- EM FX pairs: `USD/TRY`, `USD/ZAR`, `USD/BRL`, `USD/MXN`, `USD/INR`, `USD/CNH`, `USD/HKD`, `USD/SGD`, `USD/RUB`, `USD/NOK`, `USD/SEK`, `USD/DKK`, `USD/CZK`, `USD/HUF`, `USD/PLN`
- Crypto pairs: `BTC/USD`, `ETH/USD`
- Historical range: from **2010-01-01** to current date.

## Quick start

```bash
cd fx_orchestra
python scripts/download_historical.py
python -m src.main
pytest
```

## Current architecture

```text
fx_orchestra/
├── .env.example
├── pyproject.toml
├── README.md
├── docker/
│   └── docker-compose.yml
├── src/
│   ├── main.py
│   ├── config/
│   │   ├── base.py
│   │   └── schema.py
│   ├── core/
│   │   ├── types.py
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   ├── utils.py
│   │   └── redis_client.py
│   ├── data/
│   │   ├── sources/
│   │   │   ├── oanda_v20.py
│   │   │   └── economic_calendar.py
│   │   └── storage/
│   │       └── timescaledb.py
│   ├── agents/
│   │   ├── base.py
│   │   ├── tools/
│   │   │   ├── fetch_ohlcv.py
│   │   │   └── ta_indicators.py
│   │   ├── perception/technical/trend/sma.py
│   │   ├── perception/macro/region/us.py
│   │   ├── perception/sentiment/social_media/twitter.py
│   │   └── strategy/signal_fusion/technical_fusion.py
│   ├── risk/
│   │   ├── graph.py
│   │   ├── nodes/drawdown_guard.py
│   │   ├── pair_risk/eurusd_risk.py
│   │   └── risk_type/volatility_atr.py
│   ├── execution/
│   │   ├── broker/oanda_exec.py
│   │   ├── smart_orders/twap.py
│   │   └── learning/self_correction.py
│   ├── orchestrator/
│   │   ├── hybrid_flow.py
│   │   └── paper.py
│   ├── notifications/
│   │   ├── telegram.py
│   │   └── email.py
│   └── dashboard/
│       └── app.py
├── tests/
│   ├── unit/test_risk_nodes.py
│   └── integration/test_hybrid_flow.py
├── scripts/
│   ├── download_historical.py
│   └── backtest_single_pair.py
└── monitoring/
    └── prometheus.yml
```
