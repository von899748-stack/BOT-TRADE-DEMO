from risk.nodes.drawdown_guard import pass_drawdown_guard


def test_drawdown_guard_passes_under_threshold() -> None:
    assert pass_drawdown_guard([100, 110, 105, 108], max_drawdown=0.1)


def test_drawdown_guard_blocks_large_drawdown() -> None:
    assert not pass_drawdown_guard([100, 120, 80], max_drawdown=0.2)
