"""
cli.py

Provides a command-line interface for performing arithmetic
operations using the CalculatorService with structured logging.
"""

import argparse
import logging
from src.app.calculator_service import CalculatorService


def main() -> None:
    """
    Execute the calculator CLI using parsed command-line arguments.

    Optional Flags:
        --verbose : Enables DEBUG-level logging.

    Logs:
        INFO: Displays the computed result.
        ERROR: Logs division by zero or invalid input errors.
        DEBUG: Internal execution details when verbose mode is enabled.
    """
    parser = argparse.ArgumentParser(description="Simple Calculator CLI")

    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide", "power"],
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

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug-level logging",
    )

    args = parser.parse_args()

    # Configure logging level based on verbose flag
    log_level = logging.DEBUG if args.verbose else logging.INFO

    logging.basicConfig(
        level=log_level,
        format="%(levelname)s: %(message)s",
    )

    service = CalculatorService()

    try:
        logging.debug(
            "Calling service method '%s' with arguments: %s, %s",
            args.operation,
            args.first_number,
            args.second_number,
        )

        method = getattr(service, args.operation)
        result = method(args.first_number, args.second_number)

        logging.debug("Service returned result: %s", result)

        logging.info("Result: %s", result)

    except ZeroDivisionError:
        logging.error("Division by zero is not allowed.")

    except TypeError:
        logging.error("Both inputs must be integers.")


if __name__ == "__main__":
    main()
