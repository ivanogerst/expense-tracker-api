def test_login_success(client):
    client.post("/users/", json={"username": "testuser", "password": "test123"})

    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "test123"}
    )
    assert response.status_code == 200


def test_login_wrong_password(client):
    client.post("/users/", json={"username": "testuser", "password": "test123"})

    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "wrongpass"}
    )
    assert response.status_code == 401


def test_login_unknown_user(client):
    response = client.post(
        "/auth/login",
        json={"username": "ghost", "password": "whatever"}
    )
    assert response.status_code == 400