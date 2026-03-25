"""
test_cli.py

Tests for the CLI interface to verify correct execution,
error handling, and logging behavior.
"""

import sys
import pytest

from src.app.cli import main
from src.app.calculator_service import CalculatorService


def test_cli_successful_operation(monkeypatch, caplog):
    """
    Verify that a valid CLI operation logs the correct result.
    """
    monkeypatch.setattr(
        sys,
        "argv",
        ["cli.py", "add", "5", "3"],
    )

    with caplog.at_level("INFO"):
        main()

    assert "Result: 8" in caplog.text


def test_cli_division_by_zero(monkeypatch, caplog):
    """
    Verify that division by zero logs an error message.
    """
    monkeypatch.setattr(
        sys,
        "argv",
        ["cli.py", "divide", "5", "0"],
    )

    with caplog.at_level("ERROR"):
        main()

    assert "Division by zero is not allowed." in caplog.text


def test_cli_invalid_input(monkeypatch):
    """
    Verify that invalid input causes argparse to exit.
    """
    monkeypatch.setattr(
        sys,
        "argv",
        ["cli.py", "add", "a", "2"],
    )

    with pytest.raises(SystemExit):
        main()


def test_cli_history(monkeypatch, caplog, tmp_path):
    file = tmp_path / "history.json"

    def mock_service():
        return CalculatorService(history_file=file)

    monkeypatch.setattr(
        "src.app.cli.CalculatorService",
        mock_service,
    )

    monkeypatch.setattr(
        sys,
        "argv",
        ["cli.py", "history"],
    )

    with caplog.at_level("INFO"):
        main()

    assert "No operations performed yet." in caplog.text


def test_cli_clear_history(monkeypatch, caplog):
    monkeypatch.setattr(
        sys,
        "argv",
        ["cli.py", "clear_history"],
    )

    with caplog.at_level("INFO"):
        main()

    assert "History cleared successfully." in caplog.text
