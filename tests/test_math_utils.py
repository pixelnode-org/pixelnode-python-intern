import pytest
from app.math_utils import add

def test_add_two_positive_numbers():
    #Test Case 1: For two positive numebers
    assert add(2,2) == 4

def test_add_one_positive_one_zero():
    #Test case 2: one positive and one zero number edge case
    assert add(2,0) == 2

def test_add_two_negative_numbers():
    #Test case 3: Both negative numbers
    assert add(-2,-3) == -5