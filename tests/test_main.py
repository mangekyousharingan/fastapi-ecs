import pytest
from fastapi.testclient import TestClient

from src.__main__ import create_http_controller

client = TestClient(create_http_controller())


def test_health_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"result": "OK"}


@pytest.mark.parametrize(
    "name, expected_response",
    [
        ("John", {"result": "Hello John!"}),
        ("Alice", {"result": "Hello Alice!"}),
        ("Bob", {"result": "Hello Bob!"}),
    ],
)
def test_greeting_endpoint(name, expected_response):
    response = client.get(f"/greeting/{name}")

    assert response.status_code == 200
    assert response.json() == expected_response
