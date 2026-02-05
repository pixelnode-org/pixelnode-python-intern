# Function : add() For adding two numbers

"""
Provide a function for adding two numbers.
"""


def validate_integers(first_number: int, second_number: int) -> None:
    """
    Validate that both are integers.

    Parameters:
        first_number: The first number to validate.
        second_number: The second number to validate.

    Raise:
        TypeError: If either input is not integer.
    """
    if type(first_number) is not int or type(second_number) is not int:
        raise TypeError("Both inputs must be integers")


def add(first_number: int, second_number: int) -> int:
    """Return the sum of two numbers.

    Parameters:
        first_number (int): The first number.
        second_number (int): The second number.

    Returns:
        int: The sum of first_number and second_number.
    """
    validate_integers(first_number, second_number)

    return first_number + second_number
