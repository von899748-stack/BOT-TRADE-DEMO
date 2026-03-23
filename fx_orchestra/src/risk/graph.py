from __future__ import annotations

from .nodes.drawdown_guard import pass_drawdown_guard


def evaluate_risk(equity_curve: list[float]) -> bool:
    return pass_drawdown_guard(equity_curve)
