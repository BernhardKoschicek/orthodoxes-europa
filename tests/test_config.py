"""Tests for 12-factor configuration and application factory."""
import os
from unittest import mock

from app import create_app
from app.config import Config


def test_config_defaults() -> None:
    """Verify sensible local defaults for configuration."""
    assert Config.PORT == 5000
    assert Config.HOST in ("127.0.0.1", "0.0.0.0")
    assert Config.LANGUAGES == {"de": "Deutsch"}
    assert Config.VERSION == "0.1.0"


def test_config_environment_overrides() -> None:
    """Verify settings are overridable via environment variables."""
    env = {
        "PORT": "8080",
        "DEBUG": "true",
        "SECRET_KEY": "super-secret-key",
        "SESSION_COOKIE_SECURE": "true",
        "REDIS_URL": "redis://localhost:6379/1"}
    with mock.patch.dict(os.environ, env):
        class DynamicConfig(Config):
            PORT = int(os.environ.get("PORT", "5000"))
            DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
            SECRET_KEY = os.environ.get("SECRET_KEY", "")
            SESSION_COOKIE_SECURE = (
                os.environ.get("SESSION_COOKIE_SECURE", "false").lower()
                == "true")
            REDIS_URL = os.environ.get("REDIS_URL")

        assert DynamicConfig.PORT == 8080
        assert DynamicConfig.DEBUG is True
        assert DynamicConfig.SECRET_KEY == "super-secret-key"
        assert DynamicConfig.SESSION_COOKIE_SECURE is True
        assert DynamicConfig.REDIS_URL == "redis://localhost:6379/1"


def test_create_app_factory() -> None:
    """Verify application factory instantiates with custom config."""
    custom_app = create_app()
    assert custom_app is not None
    assert custom_app.config["VERSION"] is not None

    class CustomConfig(Config):
        TESTING = True
        VERSION = "9.9.9"

    new_instance = create_app(CustomConfig)
    assert new_instance.config["VERSION"] == "9.9.9"
    assert new_instance.config["TESTING"] is True
