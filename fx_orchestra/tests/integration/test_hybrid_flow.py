from config.base import build_default_config


def test_config_is_ready_for_multi_pair_hybrid_flow() -> None:
    cfg = build_default_config()

    assert cfg.metadata["strategy_mode"] == "multi-pair"
    assert cfg.timeframe == "1d"
    assert len(cfg.instruments) == 17
