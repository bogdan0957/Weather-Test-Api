from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_weather():
    """Тест с проверкой основного функционала."""
    response = client.post('/weather', json={'city': 'Москва'})
    assert response.status_code == 200
