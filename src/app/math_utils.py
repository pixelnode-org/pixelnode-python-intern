# Function : add() For adding two numbers


def validate_integers(first_number, second_number):
    """Validate that both inputs are integers.

    Parameters:
        first_number: The first input to validate.
        second_number: The second input to validate.

    Raises:
        TypeError: If either input is not an integer.
    """
    if type(first_number) is not int or type(second_number) is not int:
        raise TypeError("Both inputs must be integers.")


# Provide a function for adding two numbers.


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


# Provide a function for subtracting two numbers.


def subtract(first_number: int, second_number: int) -> int:
    """Return the difference of two numbers.
    Parameters:
        first_number (int): The first number.
        second_number (int): The second number.

    Returns:
        int: The difference of first_number and second_number."""

    validate_integers(first_number, second_number)

    return first_number - second_number


# Provide a function for multiply two numbers.


def multiply(first_number: int, second_number: int) -> int:
    """Return the difference of two numbers.
    Parameters:
        first_number (int): The first number.
        second_number (int): The second number.

    Returns:
        int: The multiplication of first_number and second_number."""

    validate_integers(first_number, second_number)

    return first_number * second_number
