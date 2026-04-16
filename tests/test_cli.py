"""
test_cli.py

Tests for the CLI interface to verify correct execution,
error handling, and logging behavior.
"""

import sys
import pytest

from app.cli import main


def test_cli_add_subcommand(monkeypatch, caplog):
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

    assert "Cannot divide by zero" in caplog.text


def test_cli_invalid_command(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["cli.py", "invalid"],
    )

    with pytest.raises(SystemExit):
        main()


def test_cli_history_subcommand(monkeypatch, caplog, tmp_path):
    file = tmp_path / "history.json"

    file.write_text("[]")

    monkeypatch.setenv("HISTORY_FILE", str(file))

    monkeypatch.setattr(
        sys,
        "argv",
        ["cli.py", "history"],
    )

    with caplog.at_level("INFO"):
        main()

    assert "No operations performed yet." in caplog.text


def test_cli_clear_history_subcom(monkeypatch, caplog):
    monkeypatch.setattr(
        sys,
        "argv",
        ["cli.py", "clear_history"],
    )

    with caplog.at_level("INFO"):
        main()

    assert "History cleared successfully." in caplog.text
