import pytest
from app.math_utils import add

def test_add_two_positive_numbers():
    assert add(2,2) == 4

def test_add_one_positive_one_zero():
    assert add(2,0) == 2

def test_add_two_negative_numbers():
    assert add(-2,-3) == -5