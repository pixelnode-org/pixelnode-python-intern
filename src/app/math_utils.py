def validate_integers(first_number: int, second_number: int) -> None:
    """
    Validate that both are integers.

    Parameters:
        first_number: The first number to validate.
        second_number: The second number to validate.

    Raises:
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


def subtract(first_number: int, second_number: int) -> int:
    """Return the subtraction of two numbers.

    Parameters:
        first_number (int): The first number.
        second_number (int): The second number.

    Returns:
        int: The subtraction of first_number and second_number.
    """
    validate_integers(first_number, second_number)

    return first_number - second_number


def multiply(first_number: int, second_number: int) -> int:
    """Return the multiplication of two numbers.

    Parameters:
        first_number (int): The first number.
        second_number (int): The second number.

    Returns:
        int: The multiplication of first_number and second_number.
    """
    validate_integers(first_number, second_number)

    return first_number * second_number


def divide(first_number: int, second_number: int) -> int:
    """Return the Division of two numbers.

    Parameters:
        first_number (int): The first number.
        second_number (int): The second number.

    Returns:
        int: The integer division of first_number by second_number.

    Raises:
        ZeroDivisionError: If second_number is 0.
    """
    validate_integers(first_number, second_number)

    if second_number == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return first_number // second_number
