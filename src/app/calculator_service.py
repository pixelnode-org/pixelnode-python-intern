"""
calculator_service.py

Provides a service layer that delegates arithmetic operations
to math_utils functions.
"""

from src.app.math_utils import add, subtract, multiply, divide, power
import json
from pathlib import Path


class CalculatorService:
    """
    Service layer responsible for delegating arithmetic operations
    and maintaining persistent operation history.

    History is stored in a JSON file and loaded on initialization.
    """

    def __init__(self, history_file: str = "history.json"):
        self.history_file = Path(history_file)
        self.max_history = 10
        self.history = self._load_history()

    def _load_history(self):
        """
        Load history from JSON file if it exists.

        Returns:
            list: Previously stored operations.
        """
        if not self.history_file.exists():
            return []

        try:
            with self.history_file.open("r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []

    def _save_history(self) -> None:
        """
        Persist current history to JSON file.
        """
        with self.history_file.open("w") as f:
            json.dump(self.history, f, indent=2)

    def _record_operation(self, operation: str, a: int, b: int, result) -> None:
        """
        Record an operation and persist it to file.
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
        Retrieve the list of recorded operations.

        Returns:
            list: A list of dictionaries representing past operations.
        """
        return self.history

    def clear_history(self) -> None:
        """
        Clear all stored history and update file.
        """
        self.history.clear()
        self._save_history()

    def add(self, a: int, b: int) -> int:
        result = add(a, b)
        self._record_operation("add", a, b, result)
        return add(a, b)

    def subtract(self, a: int, b: int) -> int:
        result = subtract(a, b)
        self._record_operation("subtract", a, b, result)
        return subtract(a, b)

    def multiply(self, a: int, b: int) -> int:
        result = multiply(a, b)
        self._record_operation("multiply", a, b, result)
        return multiply(a, b)

    def divide(self, a: int, b: int) -> float:
        result = divide(a, b)
        self._record_operation("divide", a, b, result)
        return divide(a, b)

    def power(self, a: int, b: int) -> float:
        result = power(a, b)
        self._record_operation("power", a, b, result)
        return power(a, b)
