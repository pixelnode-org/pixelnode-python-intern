def add(first_number: int, second_number: int) -> int:
    validate_integers(first_number,second_number)
    """Return the sum of two integers.

    Args:
        first_number(int): First integer
        second_number(int): Second integer

    Returns:
         int: The sum of `first_number` and `second_number`.
    """
    return first_number + second_number

def validate_integers(first_number: int, second_number: int) -> int:
    """
    validates that both inputs are integer
     
    Args:
        first_number(int): First integer to validate 
        second_number(int): Second integer to validate 

    Returns:
         show error if either of the first and second number is not integers
    
    """
    if  type(first_number) is not int and type(second_number) is not int:
        raise TypeError("both inputs must be integers")
    
        