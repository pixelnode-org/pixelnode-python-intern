import pytest
from src.app.math_utils import add


def test_add_two_positive_numbers() -> None:
    """
    Test case 1: for when adding two positive number.
    """
    assert add(2, 2) == 4


def test_add_one_positive_one_zero() -> None:
    """
    Test case 2: for when adding one positive number and zero.
    """
    assert add(2, 0) == 2


def test_add_two_negative_numbers() -> None:
    """
    Test case 3: for when adding two negative number.
    """
    assert add(-2, -3) == -5

def test_add_raises_type_error_for_mixes_types():
    """
    Test case 4: for when adding different types of value other then int.
    """
    with pytest.raises(TypeError):
        add("a",0)

def test_add_raises_type_error_for_strings():
    """
    Test case 5: for when adding two string instead of int
    """
    with pytest.raises(TypeError):
        add("a","g")
        
