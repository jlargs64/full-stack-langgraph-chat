from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    google_api_key: str
    database_url: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    auth_secret_key: str = "YOUR_SECRET_KEY_HERE"
    auth_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    env: str = "dev"

    model_config = SettingsConfigDict(env_file="../../.env")


@lru_cache
def get_settings():
    return Settings()
