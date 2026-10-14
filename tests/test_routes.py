"""Comprehensive tests for all application views and routes."""
from flask.testing import FlaskClient


def test_health_endpoint(client: FlaskClient) -> None:
    """Test health endpoint returns 200 and expected status json."""
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "ok"
    assert "version" in json_data


def test_home_page(client: FlaskClient) -> None:
    """Test home landing page renders successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Orthodoxes Europa".encode("utf-8") in response.data


def test_about_page(client: FlaskClient) -> None:
    """Test about page renders successfully."""
    response = client.get("/about")
    assert response.status_code == 200


def test_public_relations_page(client: FlaskClient) -> None:
    """Test public relations page renders successfully."""
    response = client.get("/öffentlichkeitsarbeit")
    assert response.status_code == 200
    assert "Öffentlichkeitsarbeit".encode("utf-8") in response.data


def test_publications_page(client: FlaskClient) -> None:
    """Test publications page renders successfully."""
    response = client.get("/veröffentlichungen")
    assert response.status_code == 200


def test_download_page(client: FlaskClient) -> None:
    """Test download page renders with categories."""
    response = client.get("/download")
    assert response.status_code == 200
    assert "Download".encode("utf-8") in response.data


def test_geoportal_page(client: FlaskClient) -> None:
    """Test geoportal embed page renders."""
    response = client.get("/geoportal")
    assert response.status_code == 200
    assert "Geoportal".encode("utf-8") in response.data


def test_impressum_page(client: FlaskClient) -> None:
    """Test impressum legal page renders."""
    response = client.get("/impressum")
    assert response.status_code == 200
    assert "Impressum".encode("utf-8") in response.data


def test_team_page(client: FlaskClient) -> None:
    """Test team overview page renders."""
    response = client.get("/team")
    assert response.status_code == 200
    assert "Team".encode("utf-8") in response.data


def test_projekte_overview(client: FlaskClient) -> None:
    """Test projects overview list page renders."""
    response = client.get("/projekte")
    assert response.status_code == 200
    assert "Projekte".encode("utf-8") in response.data


def test_projekt_detail_valid(client: FlaskClient) -> None:
    """Test individual project detail page renders."""
    response = client.get(
        "/projekte/Ein-Blick-in-die-gemeinsame-Vergangenheit")
    assert response.status_code == 200
    assert "Vergangenheit".encode("utf-8") in response.data


def test_404_error_page(client: FlaskClient) -> None:
    """Test non-existent route returns custom 404 response."""
    response = client.get("/this-path-does-not-exist-at-all")
    assert response.status_code == 404
    assert "404".encode("utf-8") in response.data


def test_security_headers_applied(client: FlaskClient) -> None:
    """Verify security headers are applied to responses."""
    response = client.get("/")
    assert "Strict-Transport-Security" in response.headers
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "SAMEORIGIN"
    assert response.headers["X-XSS-Protection"] == "1; mode=block"
