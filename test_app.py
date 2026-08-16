from app import app


def test_homepage_renders_pipeline_dashboard():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"CI/CD Pipeline" in response.data
    assert b"Deployment successful" in response.data
