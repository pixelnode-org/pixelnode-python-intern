import pytest
from src.app.math_utils import add
def test_add():
    #test case 1
    assert add(2, 3) == 5
    #test case 2
    assert add(5, -1) == 4



