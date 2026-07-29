"""
Farfetch ETL

validator.py
Prüft die Projektumgebung beim Programmstart.
"""

from __future__ import annotations

import os

from .logger import logger
from .paths import paths


class EnvironmentValidator:
    """
    Prüft die Projektumgebung.
    """

    @staticmethod
    def validate() -> None:
        """
        Führt alle Prüfungen aus.
        """

        logger.info("Prüfe Projektstruktur...")

        # Fehlende Ordner automatisch anlegen
        paths.create_directories()

        # Existenz prüfen
        paths.validate()

        # Schreibrechte prüfen
        EnvironmentValidator._check_write_permissions()

        logger.info("Projektstruktur erfolgreich geprüft.")

    @staticmethod
    def _check_write_permissions() -> None:
        """
        Prüft Schreibrechte auf allen relevanten Ordnern.
        """

        for directory in paths.REQUIRED_DIRECTORIES:

            test_file = directory / ".write_test"

            try:
                with open(test_file, "w", encoding="utf-8") as file:
                    file.write("ok")

                os.remove(test_file)

            except Exception as exc:
                raise PermissionError(
                    f"Keine Schreibrechte für:\n{directory}"
                ) from exc


validator = EnvironmentValidator()