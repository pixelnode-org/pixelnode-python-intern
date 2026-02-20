import pytest
from src.app.math_utils import add, subtract, multiply, divide

################################
# Valid input tests
################################


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 4),
        (2, 0, 2),
        (-2, -3, -5),
    ],
)
def test_add_returns_correct_result_for_valid_integers(
    a: int, b: int, expected: int
) -> None:
    """Verify that add() returns the correct sum for valid integer inputs."""
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 0),
        (2, 0, 2),
        (-2, -3, 1),
    ],
)
def test_subtract_returns_correct_result_for_valid_integers(
    a: int, b: int, expected: int
) -> None:
    """Verify that subtract() returns the correct difference for valid integer inputs."""
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 2, 4),
        (2, 0, 0),
        (-2, -3, 6),
    ],
)
def test_multiply_returns_correct_result_for_valid_integers(
    a: int, b: int, expected: int
) -> None:
    """Verify that multiply() returns the correct product for valid integer inputs."""
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (5, 2, 2.5),
        (-6, 3, -2.0),
    ],
)
def test_divide_returns_correct_result_for_valid_integers(
    a: int, b: int, expected: float
) -> None:
    """Verify that divide() returns the correct quotient for valid integer inputs."""
    assert divide(a, b) == expected


################################
# Invalid input tests
################################


@pytest.mark.parametrize(
    "func, a, b",
    [
        # Float cases
        (add, 2, 3.5),
        (subtract, 1.5, 2),
        (multiply, 2.0, 3),
        (divide, 10, 2.5),
        # String cases
        (add, "a", 1),
        (add, "a", "g"),
        (subtract, "a", 1),
        (multiply, "a", 1),
        (divide, "10", 2),
        # Boolean cases
        (add, True, True),
        (add, 0, True),
        (add, True, 0),
        (subtract, True, 0),
        (multiply, True, 0),
        (divide, True, 2),
    ],
)
def test_operations_raise_type_error_for_invalid_inputs(func, a, b) -> None:
    """
    Verify that all math utility functions raise TypeError
    when provided with non-integer inputs.
    """
    with pytest.raises(TypeError):
        func(a, b)

def test_divide_raises_zero_division_error():
    """Verify that divide() raises ZeroDivisionError when the divisor is 0."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)