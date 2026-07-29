"""
Farfetch ETL
Version: 0.1.0

logger.py
"""

from __future__ import annotations

import logging
from logging.handlers import TimedRotatingFileHandler

from .config import config


_LOGGER_NAME = "farfetch-etl"


def get_logger() -> logging.Logger:
    """
    Erstellt den zentralen Projekt-Logger.

    Returns
    -------
    logging.Logger
    """

    logger = logging.getLogger(_LOGGER_NAME)

    # Logger wurde bereits initialisiert
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    log_file = config.logs_dir / "farfetch.log"

    file_handler = TimedRotatingFileHandler(
        filename=log_file,
        when="midnight",
        backupCount=30,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False

    return logger


logger = get_logger()