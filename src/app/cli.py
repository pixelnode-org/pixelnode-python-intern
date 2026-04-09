"""
cli.py

Command-line interface for calculator using subcommands.
"""

import argparse
import logging

from app.calculator_service import CalculatorService
from app.config import load_config
from app.logging_config import setup_logging
from app.exceptions import CalculatorError


def main() -> None:
    """
    Execute CLI using subcommands for each operation.
    """
    parser = argparse.ArgumentParser(description="Calculator CLI with subcommands")

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging",
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, title="Available Commands"
    )

    # Helper to add arithmetic commands
    def add_operation_parser(name):
        subparser = subparsers.add_parser(
            name,
            help=(
                "raise first number to the power of second".title()
                if name == "power"
                else f"{name.title()} two numbers"
            ),
        )
        subparser.add_argument("a", type=int, help="First integer")
        subparser.add_argument("b", type=int, help="Second integer")
        return subparser

    # Arithmetic commands
    for cmd in ["add", "subtract", "multiply", "divide", "power"]:
        add_operation_parser(cmd)

    # History command
    subparsers.add_parser("history", help="Show operation history")

    # Clear history command
    subparsers.add_parser("clear_history", help="Clear operation history")

    args = parser.parse_args()

    # Setup logging
    config = load_config()
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(
        log_file=config.get("log_file", "app.log"),
        level=log_level,
    )

    service = CalculatorService(config=config)

    try:
        if args.command == "history":
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

        if args.command == "clear_history":
            service.clear_history()
            logging.info("History cleared successfully.")
            return

        # Arithmetic commands
        method = getattr(service, args.command)
        result = method(args.a, args.b)

        logging.info("Result: %s", result)

    except CalculatorError as e:
        logging.error("Error: %s", e)


if __name__ == "__main__":
    main()
