from __future__ import annotations

from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from .orchestrator.paper import run_paper


def main() -> None:
    results = run_paper()
    print(f"Generated {len(results)} paper signals")


if __name__ == "__main__":
    main()
