"""
config.py

Loads application configuration from a JSON file with safe defaults.
"""

import json
from pathlib import Path

DEFAULT_CONFIG = {
    "history_file": "history.json",
    "max_history_size": 10,
}


def load_config(config_path: str = "config.json") -> dict:
    """
    Load configuration from a JSON file.

    If file is missing or invalid, fall back to defaults.

    Parameters:
        config_path (str): Path to config file.

    Returns:
        dict: Merged configuration.
    """
    path = Path(config_path)

    if not path.exists():
        return DEFAULT_CONFIG.copy()

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return DEFAULT_CONFIG.copy()

    # Merge with defaults (missing keys fallback)
    config = DEFAULT_CONFIG.copy()
    config.update(data)

    return config
