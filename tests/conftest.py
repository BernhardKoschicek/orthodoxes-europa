"""Pytest fixtures for orthodoxes-europa tests."""
from collections.abc import Generator
import pytest
from flask.testing import FlaskClient

from app import app


@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    """Create a configured Flask test client."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client
