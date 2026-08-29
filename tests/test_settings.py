import os

from settings import Settings


def test_settings_accepts_legacy_env_names(tmp_path, monkeypatch):
    for key in [
        "OPENAI_API_KEY",
        "OPENAI_BASE_URL",
        "OPENAI_RETRIES",
        "OPENAI_TEMPERATURE",
        "OPENAI_TEMPRATURE",
        "OPENAI_TIMEOUT",
        "OPEN_AI_RETRIES",
        "OPEN_AI_TEMPERATURE",
        "OPEN_AI_TEMPRATURE",
        "OPEN_AI_TIMEOUT",
    ]:
        monkeypatch.delenv(key, raising=False)

    env_file = tmp_path / ".env"
    env_file.write_text(
        "OPENAI_API_KEY=test-key\n"
        "OPENAI_BASE_URL=https://api.openai.com/v1\n"
        "OPEN_AI_RETRIES=3\n"
        "OPEN_AI_TEMPRATURE=0.2\n"
        "OPEN_AI_TIMEOUT=60\n",
        encoding="utf-8",
    )

    settings = Settings(_env_file=env_file)

    assert settings.OPENAI_API_KEY == "test-key"
    assert settings.OPENAI_BASE_URL == "https://api.openai.com/v1"
    assert settings.OPENAI_RETRIES == 3
    assert settings.OPENAI_TEMPRATURE == 0.2
    assert settings.OPENAI_TIMEOUT == 60
