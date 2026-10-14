"""12-Factor configuration for orthodoxes-europa."""
import os
from pathlib import Path


class Config:
    """Base application configuration loaded from environment."""

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    VERSION: str = os.environ.get("APP_VERSION", "0.1.0")
    SECRET_KEY: str = os.environ.get(
        "SECRET_KEY", "dev-insecure-secret-key-change-in-production")
    DEBUG: bool = os.environ.get("DEBUG", "false").lower() in (
        "true", "1", "yes")
    HOST: str = os.environ.get("HOST", "127.0.0.1")
    PORT: int = int(os.environ.get("PORT", "5000"))

    # Storage paths
    STORAGE_PATH: Path = Path(
        os.environ.get("STORAGE_PATH", str(BASE_DIR / "storage")))
    DATA_PATH: Path = Path(
        os.environ.get("DATA_PATH", str(STORAGE_PATH / "data")))
    MEDIA_PATH: Path = Path(
        os.environ.get("MEDIA_PATH", str(STORAGE_PATH / "media")))

    # Security
    SESSION_COOKIE_SECURE: bool = os.environ.get(
        "SESSION_COOKIE_SECURE", "false").lower() in ("true", "1", "yes")
    REMEMBER_COOKIE_SECURE: bool = os.environ.get(
        "REMEMBER_COOKIE_SECURE", "true").lower() in ("true", "1", "yes")
    SESSION_COOKIE_SAMESITE: str = os.environ.get(
        "SESSION_COOKIE_SAMESITE", "Lax")

    # Optional Redis
    REDIS_URL: str | None = os.environ.get("REDIS_URL")
    LANGUAGES: dict[str, str] = {"de": "Deutsch"}
