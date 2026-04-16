"""
math_utils.py

Provides arithmetic utility functions with strict integer validation.
Includes operations such as addition, subtraction, multiplication,
division, and exponentiation.
"""

from app.core.exceptions import InvalidInputError, DivisionByZeroError


def validate_integers(first_number: int, second_number: int) -> None:
    """
    Validate that both inputs are integers.

    Parameters:
        first_number (int): First input value.
        second_number (int): Second input value.

    Raises:
        InvalidInputError: If either input is not an integer.
    """
    if type(first_number) is not int or type(second_number) is not int:
        raise InvalidInputError()


def _execute_operation(first_number: int, second_number: int, operation) -> int:
    """
    Validate inputs and execute the provided arithmetic operation.

    Parameters:
        first_number (int): The first operand.
        second_number (int): The second operand.
        operation(function) : A function that performs
            the arithmetic operation.

    Returns:
        int: The result of the provided operation.
    """
    validate_integers(first_number, second_number)
    return operation(first_number, second_number)


def add(first_number: int, second_number: int) -> int:
    """
    Return the sum of two integers.

    Parameters:
        first_number (int): First integer.
        second_number (int): Second integer.

    Returns:
        int: Sum of the two integers.

    Raises:
        InvalidInputError: If inputs are not integers.
    """
    return _execute_operation(first_number, second_number, lambda a, b: a + b)


def subtract(first_number: int, second_number: int) -> int:
    """
    Return the difference between two integers.

    Parameters:
        first_number (int): The integer to subtract from.
        second_number (int): The integer to subtract.

    Returns:
        int: The result of first_number - second_number.

    Raises:
        InvalidInputError: If inputs are not integers.
    """
    return _execute_operation(first_number, second_number, lambda a, b: a - b)


def multiply(first_number: int, second_number: int) -> int:
    """
    Return the product of two integers.

    Parameters:
        first_number (int): The first integer.
        second_number (int): The second integer.

    Returns:
        int: The result of first_number * second_number.

    Raises:
        InvalidInputError: If inputs are not integers.
    """
    return _execute_operation(first_number, second_number, lambda a, b: a * b)


def divide(first_number: int, second_number: int) -> float:
    """
    Return the result of dividing two integers.

    Parameters:
        first_number (int): Dividend.
        second_number (int): Divisor.

    Returns:
        float: Result of division.

    Raises:
        InvalidInputError: If inputs are not integers.
        DivisionByZeroError: If divisor is zero.
    """

    def division(first_number, second_number):
        if second_number == 0:
            raise DivisionByZeroError()

        return first_number / second_number

    return _execute_operation(first_number, second_number, division)


def power(first_number: int, second_number: int) -> int:
    """
    Return the result of raising first_number to the power of second_number.

    Parameters:
        first_number (int): Base value.
        second_number (int): Exponent value.

    Returns:
        float: Result of exponentiation.

    Raises:
        InvalidInputError: If inputs are not integer
    """
    return _execute_operation(first_number, second_number, lambda a, b: a**b)
