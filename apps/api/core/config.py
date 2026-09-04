from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Investor API"
    app_env: str = "development"
    app_debug: bool = True

    database_url: str
    redis_url: str

    n8n_base_url: str = "http://localhost:5678"

    tz: str = "Asia/Kolkata"
    generic_timezone: str = "Asia/Kolkata"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
