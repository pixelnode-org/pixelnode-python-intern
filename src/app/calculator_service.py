"""
calculator_service.py

Provides a service layer that delegates arithmetic operations
to math_utils functions.
"""

from src.app.math_utils import add, subtract, multiply, divide, power


class CalculatorService:
    """
    Service layer responsible for delegating arithmetic operations
    to math_utils and maintaining operation history.

    Attributes:
        history (list): Stores executed operations.
        max_history (int): Maximum number of history entries retained.
    """

    def __init__(self):
        self.history = []
        self.max_history = 10

    def _record_operation(self, operation: str, a: int, b: int, result):
        """
        Record an executed operation in the history.

        Parameters:
            operation (str): Name of the operation performed.
            a (int): First operand.
            b (int): Second operand.
            result: Result of the operation.

        Notes:
            Maintains history size within max_history limit.
        """
        self.history.append(
            {
                "operation": operation,
                "a": a,
                "b": b,
                "result": result,
            }
        )

        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get_history(self):
        """
        Retrieve the list of recorded operations.

        Returns:
            list: A list of dictionaries representing past operations.
        """
        return self.history

    def clear_history(self):
        """
        Clear all stored operation history.
        """
        self.history.clear()

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
