import pytest
from orthodoxes_europa import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Orthodoxes Europa' in response.data

def test_team_page(client):
    """Test that the team page loads correctly."""
    response = client.get('/team')
    assert response.status_code == 200
    assert b'Team' in response.data

def test_projekte_page(client):
    """Test that the projects page loads correctly."""
    response = client.get('/projekte')
    assert response.status_code == 200
    assert b'Projekte' in response.data

def test_404_page(client):
    """Test that a non-existent page returns a 404 error."""
    response = client.get('/this-page-does-not-exist')
    assert response.status_code == 404

def test_geoportal_page(client):
    """Test that the geoportal page loads correctly."""
    response = client.get('/geoportal')
    assert response.status_code == 200
    assert b'Geoportal' in response.data
    assert b'iframe' in response.data
