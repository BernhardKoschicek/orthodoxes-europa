"""Tests for template filters and utility functions."""
from app import app
from app.util.filters import (
    display_institutes,
    display_menu,
    display_sponsors)
from app.util.util import uc_first


def test_uc_first_behavior() -> None:
    """Test string capitalization utility with various inputs."""
    assert uc_first("vortrag") == "Vortrag"
    assert uc_first("") == ""
    assert uc_first(None) == ""


def test_display_menu_filter() -> None:
    """Test display_menu Jinja filter rendering and active state."""
    with app.test_request_context("/"):
        html = display_menu({}, "/projekte")
        assert "dropdown" in html
        assert "active" in html


def test_display_institutes_filter() -> None:
    """Test display_institutes filter renders logo images."""
    html = display_institutes({}, ["ZF", "ROK"])
    assert "zf_logo.jpg" in html
    assert "mantuitorul.png" in html


def test_display_sponsors_filter() -> None:
    """Test display_sponsors filter renders institute details."""
    html = display_sponsors({}, ["ZF"])
    assert "Zukunftsfonds" in html
