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


@pytest.mark.parametrize(
    "num1, num2, func",
    [("apple", 2, add), ("yellow", "black", add), (True, 2, add)],
)
def test_operation_raise_typeerror_for_invalid_input(num1, num2, func) -> None:
    """
    Verify that all math utility functions raise TypeError
    when provided with non-integer inputs.
    """
    with pytest.raises(TypeError):
        func(num1, num2)
