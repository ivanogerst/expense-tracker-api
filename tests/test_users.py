from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user(client):
    response = client.post(
        "/users/",
        json={"username": "testuser", "password": "test123"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


def test_create_user_duplicate_username(client):
    client.post("/users/", json={"username": "testuser", "password": "test123"})
    response = client.post(
        "/users/",
        json={"username": "testuser", "password": "other"}
    )
    assert response.status_code == 400


def test_get_user(client):
    create_response = client.post(
        "/users/",
        json={"username": "testuser", "password": "test123"}
    )
    user_id = create_response.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


def test_get_nonexistent_user(client):
    response = client.get("/users/9999")
    assert response.status_code == 404