"""
exceptions.py

Defines custom exception hierarchy for calculator application.
"""


class CalculatorError(Exception):
    """
    Base exception for all calculator-related errors.

    This serves as the parent class for all domain-specific exceptions
    and allows centralized error handling in higher layers such as CLI.
    """

    def __init__(self, message: str, code: str = "CALCULATOR_ERROR"):
        self.message = message
        self.code = code
        super().__init__(message)


class InvalidInputError(CalculatorError):
    """
    Raised when one or more inputs are not valid integers.

    This replaces generic TypeError to provide clearer,
    domain-specific error messaging.
    """

    def __init__(self, message="Both inputs must be integers"):
        super().__init__(message, code="INVALID_INPUT")


class DivisionByZeroError(CalculatorError):
    """
    Raised when an attempt is made to divide by zero.

    This replaces Python's built-in ZeroDivisionError to maintain
    consistent application-level error handling.
    """

    def __init__(self, message="Cannot divide by zero"):
        super().__init__(message, code="DIVISION_BY_ZERO")
