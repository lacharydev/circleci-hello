import pytest
from app.app import app as flask_app

@pytest.fixture
def client():
    flask_app.config.update({"TESTING": True})
    with flask_app.test_client() as client:
        yield client

def test_button_click_shows_message(client):
    # Load page
    r1 = client.get("/")
    assert r1.status_code == 200
    assert b"Hello CircleCI" in r1.data

    # Simulate clicking the button (POST)
    r2 = client.post("/")
    assert r2.status_code == 200
    assert b"Button clicked!" in r2.data
