# test_app.py
import pytest

from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_home_page(client):
    """ Teste l'accès à la page d'accueil """
    response = client.get('/')
    assert response.status_code == 200

def test_post_home_page(client):
    """ Teste l'envoi de formulaire """
    response = client.post('/', data={
        'number1': 10,
        'number2': 5,
        'operation': 'add'
    })
    assert response.status_code == 200
    assert b'15' in response.data
