import pytest
from src.app.math_utils import add
from src.app.math_utils import subtract
from src.app.math_utils import validate_integers

# Test cases for add function
def test_add_two_positive_numbers() -> None:
    """
    Case: for when adding two positive number.
    """
    assert add(2, 2) == 4


def test_add_one_positive_one_zero() -> None:
    """
    Case: for when adding one positive number and zero.
    """
    assert add(2, 0) == 2


def test_add_two_negative_numbers() -> None:
    """
    Case: for when adding two negative number.
    """
    assert add(-2, -3) == -5

# Test cases for subtract function
def test_subtract_two_positive_numbers() -> None:
    """
    Case: for when subtract two positive number.
    """
    assert subtract(2, 2) == 0

def test_subtract_one_positive_one_zero() -> None:
    """
    Case: for when subtract one positive number and zero.
    """
    assert subtract(2, 0) == 2


def test_subtract_two_negative_numbers() -> None:
    """
    Case: for when subtract two negative number.
    """
    assert subtract(-2, -3) == 1


def test_validate_integers_raises_type_error_for_mixes_types_strings() -> None:
    """
    Case: for when validating different types of value with strings other then int.
    """
    with pytest.raises(TypeError):
        validate_integers("a",0)

def test_validate_integers_raises_type_error_for_strings() -> None:
    """
    Case: for when validating two string instead of int
    """
    with pytest.raises(TypeError):
        validate_integers("a","g")
        
def test_validate_integers_raises_type_error_for_boolean() -> None:
    """
    Case: for when validating two boolean instead of int
    """
    with pytest.raises(TypeError):
        validate_integers(True,True)

def test_validate_integers_raises_type_error_for_mixes_types_boolean() -> None:
    """
    Case: for when validating different types of value with boolean other then int.
    """
    with pytest.raises(TypeError):
        validate_integers(0,True)
        validate_integers(True,0)