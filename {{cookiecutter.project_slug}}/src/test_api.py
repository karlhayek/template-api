""" Contains unit tests for the API file """

from starlette.testclient import TestClient
from api import app

client = TestClient(app)


def test_get_vesion():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0"}
