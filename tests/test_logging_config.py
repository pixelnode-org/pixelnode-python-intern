import logging
from app.logging_config import setup_logging


def test_logging_writes_to_file(tmp_path):
    """
    Verify that log messages are written to the specified log file.

    Steps:
    - Configure logging with a temporary log file
    - Log a message
    - Assert that the file is created and contains the message
    """
    log_file = tmp_path / "app.log"

    logging.getLogger().handlers.clear()
    setup_logging(log_file=str(log_file))

    assert log_file.exists()
    logging.info("Test log")

    content = log_file.read_text()
    assert "Test log" in content


def test_logging_no_duplicate_handlers(tmp_path):
    """
    Verify that multiple calls to setup_logging do not create duplicate handlers.

    Steps:
    - Configure logging twice
    - Log a message
    - Assert that the message appears only once in the log file
    """
    log_file = tmp_path / "app.log"

    logging.getLogger().handlers.clear()
    setup_logging(log_file=str(log_file))
    setup_logging(log_file=str(log_file))  # called twice
    logging.info("Hello")

    content = log_file.read_text()

    # Should appear only once
    assert content.count("Hello") == 1
