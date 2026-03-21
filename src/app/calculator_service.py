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

    def __init__(self):
        self.history = []

    def _record_operation(self, operation: str, a: int, b: int, result):
        """
        Store a record of a performed operation in history.

        Parameters:
            operation (str): Name of the operation performed.
            a (int): First input value.
            b (int): Second input value.
            result: Result of the operation.
        """
        self.history.append(
            {
                "operation": operation,
                "inputs": [a, b],
                "result": result,
            }
        )

    def get_history(self):
        """
        Return the list of all recorded operations.

        Returns:
            list: List of dictionaries containing operation details.
        """
        return self.history

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
