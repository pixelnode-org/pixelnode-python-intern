"""
logging_config.py

Centralized logging configuration for console and file outputs.
"""

import logging
import logging.handlers
from pathlib import Path


def setup_logging(log_file: str = "app.log", level: int = logging.INFO) -> None:
    """
    Configure logging with both console and file handlers.

    Parameters:
        log_file (str): Path to the log file.
        level (int): Logging level (INFO, DEBUG, etc.)
    """
    logger = logging.getLogger()

    # Prevent duplicate handlers if called multiple times
    if logger.handlers:
        return

    logger.setLevel(level)

    formatter = logging.Formatter("%(levelname)s: %(message)s")

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)

    # File handler (auto-creates file)
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=1_000_000,  # 1 MB
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
