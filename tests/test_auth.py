from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app

client = TestClient(app)


def test_register():
    response = client.post("/users/register", json={
        "username": "testuser",
        "email": "test@mail.com",
        "password": "123"
    })

    assert response.status_code == 200


def test_login():
    response = client.post("/users/login", json={
        "username": "testuser",
        "password": "123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()
