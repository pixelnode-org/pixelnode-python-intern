"""
history_manager.py

Handles persistent storage and management of calculator operation history.
"""

import json
from pathlib import Path


class HistoryManager:
    """
    Manages loading, storing, and clearing operation history using a JSON file.
    """

    def __init__(self, history_file: str, max_history: int):
        self.history_file = Path(history_file)
        self.max_history = max_history
        self.history = self._load_history()

    def _load_history(self):
        """
        Load history from JSON file if it exists.

        Returns:
            list: Stored operations.
        """
        if not self.history_file.exists():
            return []

        try:
            with self.history_file.open("r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []

    def _save_history(self) -> None:
        """
        Persist current history to JSON file.
        """
        with self.history_file.open("w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2)

    def add_operation(self, operation: str, a: int, b: int, result) -> None:
        """
        Add a new operation to history and persist it.

        Parameters:
            operation (str): Operation name.
            a (int): First operand.
            b (int): Second operand.
            result: Operation result.
        """
        entry = {
            "operation": operation,
            "a": a,
            "b": b,
            "result": result,
        }

        self.history.append(entry)

        if len(self.history) > self.max_history:
            self.history.pop(0)

        self._save_history()

    def get_history(self):
        """
        Return stored history.

        Returns:
            list: List of operation entries.
        """
        return self.history

    def clear_history(self) -> None:
        """
        Clear all stored history and update file.
        """
        self.history.clear()
        self._save_history()
