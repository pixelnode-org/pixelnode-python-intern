"""
test_calculator_service.py

Tests for the CalculatorService class to verify correct delegation
to math_utils functions and proper exception propagation.
"""

import pytest
from src.app.calculator_service import CalculatorService


@pytest.fixture
def calculator():
    """
    Provide a fresh instance of CalculatorService
    for each test case.
    """
    return CalculatorService()


def test_service_add_delegates_correctly(calculator):
    """Verify that add() correctly delegates to math_utils.add."""
    assert calculator.add(2, 3) == 5


def test_service_subtract_delegates_correctly(calculator):
    """Verify that subtract() correctly delegates to math_utils.subtract."""
    assert calculator.subtract(5, 2) == 3


def test_service_multiply_delegates_correctly(calculator):
    """Verify that multiply() correctly delegates to math_utils.multiply."""
    assert calculator.multiply(4, 3) == 12


def test_service_divide_delegates_correctly(calculator):
    """Verify that divide() correctly delegates to math_utils.divide."""
    assert calculator.divide(8, 2) == 4


def test_service_propagates_type_error(calculator):
    """
    Verify that TypeError raised by math_utils
    is propagated through the service layer.
    """
    with pytest.raises(TypeError):
        calculator.add("a", 2)


def test_service_propagates_zero_division(calculator):
    """
    Verify that ZeroDivisionError raised by math_utils
    is propagated through the service layer.
    """
    with pytest.raises(ZeroDivisionError):
        calculator.divide(4, 0)
