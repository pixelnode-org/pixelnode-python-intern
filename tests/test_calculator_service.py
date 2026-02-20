import pytest
from src.app.calculator_service import CalculatorService


@pytest.fixture
def calculator():
    return CalculatorService()


def test_service_add_delegates_correctly(calculator):
    assert calculator.add(2, 3) == 5


def test_service_subtract_delegates_correctly(calculator):
    assert calculator.subtract(5, 2) == 3


def test_service_multiply_delegates_correctly(calculator):
    assert calculator.multiply(4, 3) == 12


def test_service_divide_delegates_correctly(calculator):
    assert calculator.divide(8, 2) == 4


def test_service_propagates_type_error(calculator):
    with pytest.raises(TypeError):
        calculator.add("a", 2)


def test_service_propagates_zero_division(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(4, 0)