import pytest
from app.math_utils import add

def test_add_two_positive_numbers():
    '''
    Test case for when adding two positive number.
    '''
    assert add(2,2) == 4

def test_add_one_positive_one_zero():
    '''
    Test case for when adding one positive number and zero.
    '''
    assert add(2,0) == 2

def test_add_two_negative_numbers():
    '''
    Test case for when adding two negative number.
    '''
    assert add(-2,-3) == -5