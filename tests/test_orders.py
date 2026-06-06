from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app

client = TestClient(app)


def test_create_order():
    login = client.post("/users/login", json={
        "username": "testuser",
        "password": "123"
    })

    token = login.json()["access_token"]

    response = client.post(
        "/orders",
        json={
            "title": "test order",
            "description": "test"
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
