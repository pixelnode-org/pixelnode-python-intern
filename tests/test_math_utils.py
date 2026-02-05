import pytest
from src.app.math_utils import add


def test_add_two_positive_numbers():
    # Test Case 1: For two positive numebers
    assert add(2, 2) == 4


def test_add_one_positive_one_zero():
    # Test case 2: one positive and one zero number edge case
    assert add(2, 0) == 2


def test_add_two_negative_numbers():
    # Test case 3: Both negative numbers
    assert add(-2, -3) == -5

def test_add_raises_type_error_for_strings():
    # Test case 4: Both inputs are strings
    with pytest.raises(TypeError):
        add("a", "a")

def test_add_raises_type_error_for_mixed_types_strings():
    # Test case 5: One input is string, other is integer
    with pytest.raises(TypeError):
        add("a", 0)
        add(0, "a")

def test_add_raises_type_error_for_boolean():
    # Test case 6: Both input is boolean
    with pytest.raises(TypeError):
        add(True, False)

def test_add_raises_type_error_for_mixed_types_boolean():
    # Test case 7: One input is boolean, other is integer
    with pytest.raises(TypeError):
        add(True, 5)
        add(5, True)