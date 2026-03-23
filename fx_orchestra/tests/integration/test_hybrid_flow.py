from orchestrator.hybrid_flow import run_hybrid_flow


def test_hybrid_flow_builds_signal_for_all_symbols() -> None:
    results = run_hybrid_flow()
    assert len(results) == 17
    assert {r["symbol"] for r in results} >= {"USD/TRY", "BTC/USD", "ETH/USD"}
