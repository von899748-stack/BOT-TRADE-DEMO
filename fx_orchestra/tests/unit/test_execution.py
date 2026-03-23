from execution.learning.self_correction import adjust_confidence


def test_adjust_confidence_clamps_values() -> None:
    assert adjust_confidence(0.95, -0.9) >= 0
    assert adjust_confidence(0.2, 0.9) <= 1
