from __future__ import annotations


def pass_drawdown_guard(equity_curve: list[float], max_drawdown: float = 0.2) -> bool:
    if not equity_curve:
        return True
    peak = equity_curve[0]
    worst_dd = 0.0
    for value in equity_curve:
        peak = max(peak, value)
        dd = (peak - value) / peak if peak > 0 else 0.0
        worst_dd = max(worst_dd, dd)
    return worst_dd <= max_drawdown
