"""
Farfetch ETL

main.py
Programmeinstieg
"""

from __future__ import annotations

import sys
import time

from core.logger import logger
from core.validator import validator


def main() -> int:

    start = time.perf_counter()

    logger.info("=" * 60)
    logger.info("Farfetch ETL gestartet")

    try:

        validator.validate()

        logger.info("Initialisierung erfolgreich abgeschlossen.")

    except Exception:

        logger.exception("Programm mit Fehler beendet.")
        return 1

    runtime = time.perf_counter() - start

    logger.info(f"Laufzeit: {runtime:.2f} Sekunden")
    logger.info("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())