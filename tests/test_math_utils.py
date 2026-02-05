import pytest
from src.app.math_utils import add
from src.app.math_utils import validate_integers


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

def test_add_raises_type_error_for_mixes_types_strings():
    """
    Test case 4: for when adding different types of value with strings other then int.
    """
    with pytest.raises(TypeError):
        add("a",0)

def test_add_raises_type_error_for_strings():
    """
    Test case 5: for when adding two string instead of int
    """
    with pytest.raises(TypeError):
        add("a","g")
        
def test_add_raises_type_error_for_boolean():
    """
    Test case 6: for when adding two boolean instead of int
    """
    with pytest.raises(TypeError):
        add(True,True)

def test_add_raises_type_error_for_mixes_types_boolean():
    """
    Test case 7: for when adding different types of value with boolean other then int.
    """
    with pytest.raises(TypeError):
        add(0,True)
        add(True,0)