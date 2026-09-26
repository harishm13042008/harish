from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ComicCraft AI"
    panel_count: int = 5
    gemini_api_key: str | None = None
    gemini_outline_model: str = "gemini-3.8-flash"
    gemini_image_model: str = "imagen-3.0-generate-002"
    gemini_story_model: str = "gemini-3.8-flash"
    demo_mode: bool = False
    image_provider: str = "gemini"
    hf_token: str | None = None
    image_model: str = "black-forest-labs/FLUX.1-schnell"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


def ensure_directories() -> None:
    Path("static").mkdir(exist_ok=True)
    Path("static/generated").mkdir(parents=True, exist_ok=True)
