from pathlib import Path

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    OPENAI_API_KEY: str
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"
    OPENAI_RETRIES: int = Field(
        default=3,
        validation_alias=AliasChoices(
            "OPENAI_RETRIES",
            "OPEN_AI_RETRIES",
            "open_ai_retries",
        ),
    )
    OPENAI_TEMPRATURE: float = Field(
        default=0.2,
        validation_alias=AliasChoices(
            "OPENAI_TEMPRATURE",
            "OPEN_AI_TEMPRATURE",
            "open_ai_temprature",
            "OPENAI_TEMPERATURE",
            "OPEN_AI_TEMPERATURE",
        ),
    )
    OPENAI_TIMEOUT: int = Field(
        default=60,
        validation_alias=AliasChoices(
            "OPENAI_TIMEOUT",
            "OPEN_AI_TIMEOUT",
            "open_ai_timeout",
        ),
    )


my_settings = Settings()