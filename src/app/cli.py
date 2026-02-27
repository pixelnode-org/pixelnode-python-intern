"""
cli.py

Provides a command-line interface for performing arithmetic
operations using the CalculatorService.
"""

import argparse
import logging
from src.app.calculator_service import CalculatorService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)


def main() -> None:
    """
    Execute the calculator CLI using parsed command-line arguments.

    Logs:
        INFO: Displays the computed result.
        ERROR: Logs division by zero or invalid input errors.
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
        logging.info("Result: %s", result)

    except ZeroDivisionError:
        logging.error("Division by zero is not allowed.")

    except TypeError:
        logging.error("Both inputs must be integers.")


if __name__ == "__main__":
    main()
