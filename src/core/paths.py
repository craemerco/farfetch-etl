"""
Farfetch ETL
Version: 0.1.0

Datei:
    paths.py

Beschreibung:
    Verwaltet alle Projektverzeichnisse und erstellt sie bei Bedarf automatisch.
"""

from __future__ import annotations

from pathlib import Path

from .config import config


class ProjectPaths:
    """
    Verwaltet sämtliche Projektordner.
    """

    REQUIRED_DIRECTORIES = (
        config.input_dir,
        config.output_dir,
        config.archive_dir,
        config.logs_dir,
        config.config_dir,
        config.mappings_dir,
        config.tests_dir,
    )

    @staticmethod
    def create_directories() -> None:
        """
        Erstellt alle benötigten Projektordner.
        Bereits vorhandene Ordner bleiben unverändert.
        """
        for directory in ProjectPaths.REQUIRED_DIRECTORIES:
            directory.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def validate() -> None:
        """
        Prüft, ob alle Projektordner existieren.

        Raises
        ------
        FileNotFoundError
            Falls ein Ordner fehlt.
        """
        missing = [
            directory
            for directory in ProjectPaths.REQUIRED_DIRECTORIES
            if not directory.exists()
        ]

        if missing:
            raise FileNotFoundError(
                "Folgende Projektordner fehlen:\n"
                + "\n".join(str(path) for path in missing)
            )

    @staticmethod
    def print_overview() -> None:
        """
        Gibt sämtliche Projektordner aus.
        """

        print("\nProjektverzeichnisse\n")

        for directory in ProjectPaths.REQUIRED_DIRECTORIES:
            print(f"✓ {directory}")


paths = ProjectPaths()