from src.app.config import load_config


def test_load_config_from_file(tmp_path):
    config_file = tmp_path / "config.json"

    config_file.write_text('{"history_file": "test.json", "max_history_size": 5}')

    config = load_config(config_file)

    assert config["history_file"] == "test.json"
    assert config["max_history_size"] == 5


def test_load_config_defaults(tmp_path):
    config_file = tmp_path / "missing.json"

    config = load_config(config_file)

    assert config["history_file"] == "history.json"
    assert config["max_history_size"] == 10


def test_partial_config(tmp_path):
    config_file = tmp_path / "config.json"

    config_file.write_text('{"history_file": "custom.json"}')

    config = load_config(config_file)

    assert config["history_file"] == "custom.json"
    assert config["max_history_size"] == 10  # fallback


def test_env_overrides_config(tmp_path, monkeypatch):
    config_file = tmp_path / "config.json"

    config_file.write_text('{"history_file": "file.json", "log_file": "file.log"}')

    monkeypatch.setenv("HISTORY_FILE", "env_history.json")
    monkeypatch.setenv("LOG_FILE", "env_log.log")

    config = load_config(config_file)

    assert config["history_file"] == "env_history.json"
    assert config["log_file"] == "env_log.log"


def test_config_used_when_no_env(tmp_path):
    config_file = tmp_path / "config.json"

    config_file.write_text('{"history_file": "file.json", "log_file": "file.log"}')

    config = load_config(config_file)

    assert config["history_file"] == "file.json"
    assert config["log_file"] == "file.log"


def test_defaults_when_no_config_and_no_env(tmp_path):
    config_file = tmp_path / "missing.json"

    config = load_config(config_file)

    assert config["history_file"] == "history.json"
    assert config["log_file"] == "app.log"
