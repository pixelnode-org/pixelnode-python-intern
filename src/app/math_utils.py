"""
math_utils.py

Provides basic arithmetic utility functions including addition,
subtraction, multiplication, and division with strict integer validation.
"""


def validate_integers(first_number: int, second_number: int) -> None:
    """
    Validate that both inputs are of the integer type.

    Parameters:
        first_number: The first value to check.
        second_number: The second value to check.

    Raises:
        TypeError: If either input is not an instance of int.
    """
    if type(first_number) is not int or type(second_number) is not int:
        raise TypeError("Both inputs must be integers")


def _execute_operation(first_number: int, second_number: int, operation) -> int :
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
        first_number (int): The first integer.
        second_number (int): The second integer.

    Returns:
        int: The sum of first_number and second_number.
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
    """
    return _execute_operation(first_number, second_number, lambda a, b: a * b)


def divide(first_number: int, second_number: int) -> float:
    """
    Return the quotient of two integers as a float.

    Parameters:
        first_number (int): The dividend.
        second_number (int): The divisor.

    Returns:
        float: The result of first_number / second_number.

    Raises:
        ZeroDivisionError: If the second_number is zero.
    """

    def division(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    return _execute_operation(first_number, second_number, division)
