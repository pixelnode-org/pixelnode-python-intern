"""
calculator_service.py

Provides a service layer that delegates arithmetic operations
to math_utils functions.
"""

from src.app.math_utils import add, subtract, multiply, divide, power


class CalculatorService:
    """
    Service layer for arithmetic operations.

    This class delegates arithmetic operations to the underlying
    math_utils module without duplicating logic.
    """

    def add(self, a: int, b: int) -> int:
        return add(a, b)

    def subtract(self, a: int, b: int) -> int:
        return subtract(a, b)

    def multiply(self, a: int, b: int) -> int:
        return multiply(a, b)

    def divide(self, a: int, b: int) -> float:
        return divide(a, b)

    def power(self, a: int, b: int) -> float:
        return power(a, b)
