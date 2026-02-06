import pytest
from src.app.math_utils import add, sub, validate_integers

###############################################
# Test case function for Addition
##############################################


def test_add_two_positive_numbers():
    # Test Case 1: For two positive numebers
    assert add(2, 2) == 4


def test_add_one_positive_one_zero():
    # Test case 2: one positive and one zero number edge case
    assert add(2, 0) == 2


def test_add_two_negative_numbers():
    # Test case 3: Both negative numbers
    assert add(-2, -3) == -5


###############################################
# Test case function for Subtraction
##############################################


def test_sub_two_positive_numbers():
    # Test Case 4: For two positive numebers
    assert sub(2, 2) == 0


def test_sub_one_positive_one_zero():
    # Test case 5: one positive and one zero number edge case
    assert sub(2, 0) == 2


def test_sub_two_negative_numbers():
    # Test case 6: Both negative numbers
    assert sub(-2, -3) == 1


############################################################
# Error Handling function for Math Utility module
###########################################################


def test_validate_raises_type_error_for_strings():
    # Test case 7: Both inputs are strings
    with pytest.raises(TypeError):
        validate_integers("a", "a")


def test_validate_raises_type_error_for_mixed_types_strings():
    # Test case 8: One input is string, other is integer
    with pytest.raises(TypeError):
        validate_integers("a", 0)
        validate_integers(0, "a")


def test_validate_raises_type_error_for_boolean():
    # Test case 9: Both input is boolean
    with pytest.raises(TypeError):
        validate_integers(True, False)


def test_validate_raises_type_error_for_mixed_types_boolean():
    # Test case 10: One input is boolean, other is integer
    with pytest.raises(TypeError):
        validate_integers(True, 5)
        validate_integers(5, True)
