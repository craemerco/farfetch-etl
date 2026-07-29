"""
Farfetch ETL
Configuration Management

Author: Andreas Kessler
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectConfig:
    """
    Zentrale Projektkonfiguration.

    Alle Pfade werden relativ zum Projektverzeichnis aufgebaut.
    """

    project_root: Path

    @property
    def input_dir(self) -> Path:
        return self.project_root / "input"

    @property
    def output_dir(self) -> Path:
        return self.project_root / "output"

    @property
    def archive_dir(self) -> Path:
        return self.project_root / "archive"

    @property
    def logs_dir(self) -> Path:
        return self.project_root / "logs"

    @property
    def config_dir(self) -> Path:
        return self.project_root / "config"

    @property
    def mappings_dir(self) -> Path:
        return self.config_dir / "mappings"

    @property
    def tests_dir(self) -> Path:
        return self.project_root / "tests"


def get_project_root() -> Path:
    """
    Ermittelt automatisch das Projektverzeichnis.

    Returns
    -------
    Path
        Root-Verzeichnis des Projektes.
    """
    return Path(__file__).resolve().parents[2]


config = ProjectConfig(
    project_root=get_project_root()
)