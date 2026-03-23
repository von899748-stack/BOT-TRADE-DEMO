from __future__ import annotations

from orchestrator.paper import run_paper


def main() -> None:
    results = run_paper()
    print(f"Generated {len(results)} paper signals")


if __name__ == "__main__":
    main()
