# Function : add() For adding two numbers

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

    if not isinstance(first_number, int) or not isinstance(second_number, int):
        raise TypeError("Both inputs must be integers")
    
    return first_number + second_number