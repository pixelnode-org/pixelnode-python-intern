# Function : add() For adding two numbers


def validate_integers(first_number, second_number):
    """Validate that both inputs are integers.

    Parameters:
        first_number: The first input to validate.
        second_number: The second input to validate.

    Raises:
        TypeError: If either input is not an integer.
    """
    if not isinstance(first_number, int) or not isinstance(second_number, int):
        raise TypeError("Both inputs must be integers.")
    

"""
Provide a function for adding two numbers.
"""


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

