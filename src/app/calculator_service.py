"""
calculator_service.py

Provides a service layer that delegates arithmetic operations
to math_utils functions.
"""

from src.app.math_utils import add, subtract, multiply, divide, power
from src.app.history_manager import HistoryManager


class CalculatorService:
    """
    Service layer responsible for delegating arithmetic operations
    and maintaining persistent operation history.

    History is stored in a JSON file and loaded on initialization.
    """

    def __init__(self, history_manager=None):
        self.history_manager = history_manager or HistoryManager()

    def get_history(self):
        return self.history_manager.get_history()

    def clear_history(self):
        self.history_manager.clear_history()

    def add(self, a: int, b: int) -> int:
        result = add(a, b)
        self.history_manager.add_operation("add", a, b, result)
        return add(a, b)

    def subtract(self, a: int, b: int) -> int:
        result = subtract(a, b)
        self.history_manager.add_operation("subtract", a, b, result)
        return subtract(a, b)

    def multiply(self, a: int, b: int) -> int:
        result = multiply(a, b)
        self.history_manager.add_operation("multiply", a, b, result)
        return multiply(a, b)

    def divide(self, a: int, b: int) -> float:
        result = divide(a, b)
        self.history_manager.add_operation("divide", a, b, result)
        return divide(a, b)

    def power(self, a: int, b: int) -> float:
        result = power(a, b)
        self.history_manager.add_operation("power", a, b, result)
        return power(a, b)
