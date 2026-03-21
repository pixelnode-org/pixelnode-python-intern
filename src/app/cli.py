"""
cli.py

Command-line interface for performing arithmetic operations
using CalculatorService with structured logging.
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
        choices=["add", "subtract", "multiply", "divide", "power", "history"],
        help="Arithmetic operation to perform",
    )

    parser.add_argument(
        "first_number",
        type=int,
        nargs="?",
        help="First integer value",
    )

    parser.add_argument(
        "second_number",
        type=int,
        nargs="?",
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

        if args.operation == "history":
            history = service.get_history()

            if not history:
                logging.info("No operations performed yet.")

            for i, entry in enumerate(history, start=1):
                logging.info(
                    "%d. %s %s = %s",
                    i,
                    entry["operation"],
                    entry["inputs"],
                    entry["result"],
                )

            return

        # Validate inputs for other operations
        if args.first_number is None or args.second_number is None:
            logging.error("Both numbers are required for this operation.")
            return

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
