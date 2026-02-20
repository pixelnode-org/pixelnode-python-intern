import pytest
from src.app.math_utils import add


############################
# valid input tests
############################
@pytest.mark.parametrize("num1, num2, expected", [(2, 3, 5), (5, 0, 5), (-1, -1, -2)])
def test_add_returns_correct_result_for_valid_integers(
    num1: int, num2: int, expected: int
) -> None:
    """ 
    verify that add()returns the correct results for valid integer inputs
    """
    assert add(num1, num2) == expected
