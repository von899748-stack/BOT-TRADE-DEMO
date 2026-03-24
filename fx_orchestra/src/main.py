"""Entry point for FX Orchestra scaffold."""

from config.base import build_default_config


def main() -> None:
    cfg = build_default_config()
    print("fx_orchestra scaffold is ready")
    print(f"Pairs configured: {len(cfg.instruments)}")
    print(f"History window: {cfg.history.start} -> {cfg.history.end}")


if __name__ == "__main__":
    main()
