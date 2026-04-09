"""
test_calculator_service.py

Tests for the CalculatorService class to verify correct delegation
to math_utils functions and proper exception propagation.
"""

import pytest
from app.calculator_service import CalculatorService
from app.exceptions import InvalidInputError, DivisionByZeroError


@pytest.fixture
def calculator():
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


def test_service_power_delegates_correctly(calculator):
    """Verify that power() correctly delegates to math_utils.divide."""
    assert calculator.power(2, 3) == 8


def test_service_propagates_invalid_i_error(calculator):
    """
    Verify that InvalidInputError raised by math_utils
    is propagated through the service layer.
    """
    with pytest.raises(InvalidInputError):
        calculator.add("a", 2)


def test_service_propagates_zero_division(calculator):
    """
    Verify that DivisionByZeroError raised by math_utils
    is propagated through the service layer.
    """
    with pytest.raises(DivisionByZeroError):
        calculator.divide(4, 0)


def test_clear_history(calculator):
    calculator.add(2, 3)
    calculator.clear_history()

    assert len(calculator.get_history()) == 0


def test_history_records_operations(calculator):
    """
    Verify that each calculator operation is recorded correctly
    in the service history.

    Ensures:
    - Operations are appended in order
    - Stored operation names match executed methods
    """
    calculator.add(2, 3)
    calculator.multiply(4, 5)

    history = calculator.get_history()

    assert len(history) == 2
    assert history[0]["operation"] == "add"
    assert history[1]["operation"] == "multiply"
