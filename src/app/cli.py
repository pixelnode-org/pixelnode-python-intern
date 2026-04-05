"""
cli.py

Command-line interface for performing arithmetic operations
using CalculatorService with structured logging.
"""

import argparse
import logging
from src.app.config import load_config
from src.app.calculator_service import CalculatorService
from src.app.logging_config import setup_logging


def main() -> None:
    """
    Execute the calculator CLI using parsed command-line arguments.

    Supported operations:
        - add, subtract, multiply, divide, power
        - history: display past operations
        - clear_history: clear stored history

    Optional flags:
        --verbose : Enables DEBUG-level logging

    Logs:
        INFO: Displays results and history
        ERROR: Logs runtime errors (e.g., division by zero)
        DEBUG: Internal execution details (verbose mode)
    """
    parser = argparse.ArgumentParser(description="Simple Calculator CLI")

    parser.add_argument(
        "operation",
        choices=[
            "add",
            "subtract",
            "multiply",
            "divide",
            "power",
            "history",
            "clear_history",
        ],
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

    config = load_config()

    log_level = logging.DEBUG if args.verbose else logging.INFO

    setup_logging(
        log_file=config.get("log_file", "app.log"),
        level=log_level,
    )

    service = CalculatorService(config=config)

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
                return

            logging.info("Operation History:")

            for i, entry in enumerate(history, start=1):
                logging.info(
                    "%d. %s(%s, %s) = %s",
                    i,
                    entry["operation"],
                    entry["a"],
                    entry["b"],
                    entry["result"],
                )
            return

        if args.operation == "clear_history":
            service.clear_history()
            logging.info("History cleared successfully.")
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
