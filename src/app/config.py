"""
config.py

Loads application configuration from environment variables,
config file, and defaults with proper precedence.
"""

import json
import os
from pathlib import Path

DEFAULT_CONFIG = {
    "history_file": "history.json",
    "max_history_size": 10,
    "log_file": "app.log",
}


def load_config(config_path: str = "config.json") -> dict:
    """
    Load configuration with precedence:
    environment variables > config file > defaults

    Parameters:
        config_path (str): Path to config file

    Returns:
        dict: Final configuration
    """
    config = DEFAULT_CONFIG.copy()

    # Step 1: Load from config file
    path = Path(config_path)

    if path.exists():
        try:
            with path.open("r", encoding="utf-8") as f:
                file_config = json.load(f)
                config.update(file_config)
        except (json.JSONDecodeError, OSError):
            pass  # fallback to defaults

    # Step 2: Override with environment variables
    env_history_file = os.environ.get("HISTORY_FILE")
    env_log_file = os.environ.get("LOG_FILE")

    if env_history_file:
        config["history_file"] = env_history_file

    if env_log_file:
        config["log_file"] = env_log_file

    return config
