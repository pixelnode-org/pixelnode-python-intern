"""
cli.py

Provides a command-line interface for performing arithmetic
operations using the CalculatorService.
"""

import argparse
from src.app.calculator_service import CalculatorService


def main() -> None:
    """
    Parse command-line arguments and execute the requested
    arithmetic operation using CalculatorService.

    Expected arguments:
        operation: One of (add, subtract, multiply, divide)
        first_number: First integer operand
        second_number: Second integer operand

    Prints:
        The result of the operation.

    Handles:
        ZeroDivisionError: If division by zero is attempted.
    """
    parser = argparse.ArgumentParser(description="Simple Calculator CLI")

    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="Arithmetic operation to perform",
    )

    parser.add_argument(
        "first_number",
        type=int,
        help="First integer value",
    )

    parser.add_argument(
        "second_number",
        type=int,
        help="Second integer value",
    )

    args = parser.parse_args()

    service = CalculatorService()

    try:
        method = getattr(service, args.operation)
        result = method(args.first_number, args.second_number)
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


if __name__ == "__main__":
    main()
