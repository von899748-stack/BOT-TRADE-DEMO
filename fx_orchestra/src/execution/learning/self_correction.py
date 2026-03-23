from __future__ import annotations


def adjust_confidence(base_confidence: float, feedback: float) -> float:
    """Apply bounded additive update."""

    value = base_confidence + feedback * 0.2
    return max(0.0, min(1.0, value))
