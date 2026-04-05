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
