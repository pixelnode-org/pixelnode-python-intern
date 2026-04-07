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


class InvalidInputError(CalculatorError):
    """
    Raised when one or more inputs are not valid integers.

    This replaces generic TypeError to provide clearer,
    domain-specific error messaging.
    """


class DivisionByZeroError(CalculatorError):
    """
    Raised when an attempt is made to divide by zero.

    This replaces Python's built-in ZeroDivisionError to maintain
    consistent application-level error handling.
    """
