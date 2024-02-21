import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """ Test pour la page d'accueil. """
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
