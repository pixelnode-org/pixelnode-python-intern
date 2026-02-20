# src/app/calculator_service.py

from src.app.math_utils import add, subtract, multiply, divide


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

    def divide(self, a: int, b: int) -> int:
        return divide(a, b)