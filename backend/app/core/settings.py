from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    google_api_key: str
    database_url: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    env: str = "dev"

    model_config = SettingsConfigDict(env_file="../../.env")


@lru_cache
def get_settings():
    return Settings()
