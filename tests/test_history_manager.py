"""
Tests for HistoryManager functionality.

Covers operation recording, persistence, and clearing behavior.
"""

from app.history_manager import HistoryManager


def test_history_manager_add_operation(tmp_path):
    """Verify that an operation is correctly stored in history."""
    file = tmp_path / "history.json"

    manager = HistoryManager(history_file=file, max_history=10)
    manager.add_operation("add", 2, 3, 5)

    history = manager.get_history()

    assert len(history) == 1

    entry = history[0]
    assert entry["operation"] == "add"
    assert entry["a"] == 2
    assert entry["b"] == 3
    assert entry["result"] == 5


def test_history_manager_clear(tmp_path):
    """Verify that history is cleared and no entries remain."""
    file = tmp_path / "history.json"

    manager = HistoryManager(history_file=file, max_history=10)
    manager.add_operation("add", 1, 1, 2)

    manager.clear_history()

    assert len(manager.get_history()) == 0


def test_history_manager_persistence(tmp_path):
    """Verify that history persists across service instances."""
    file = tmp_path / "history.json"

    manager = HistoryManager(history_file=file, max_history=10)
    manager.add_operation("add", 2, 3, 5)

    new_manager = HistoryManager(history_file=file, max_history=10)

    history = new_manager.get_history()

    assert len(history) == 1
    assert history[0]["result"] == 5
