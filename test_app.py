from app import app


def test_homepage_returns_running_message():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"CI/CD Project Running"
