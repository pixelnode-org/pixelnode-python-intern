import pytest
from fastapi.testclient import TestClient
from app.api import app


@pytest.fixture
def client():
    """
    Provides a FastAPI test client for API testing.
    """
    return TestClient(app)


def test_add_valid(client):
    """
    Verify that valid input returns correct result.
    """
    response = client.post("/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_add_invalid_type(client):
    """
    Verify that invalid input type triggers validation error (422).
    """
    response = client.post("/add", json={"a": "x", "b": 3})
    assert response.status_code == 422


def test_divide_by_zero(client):
    """
    Verify that division by zero is handled as a domain error (400).
    """
    response = client.post("/divide", json={"a": 5, "b": 0})
    assert response.status_code == 400
