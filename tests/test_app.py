import os
import tempfile
import pytest

@pytest.fixture()
def client(monkeypatch):
    db_file = tempfile.NamedTemporaryFile(delete=False)
    db_file.close()

    import database
    import app as app_module

    monkeypatch.setattr(database, "DB_PATH", database.Path(db_file.name))
    database.init_db()

    app_module.app.config.update(TESTING=True)
    with app_module.app.test_client() as client:
        yield client

    os.unlink(db_file.name)

def test_homepage_lists_providers(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Dr. Asha Mehta" in response.data

def test_book_appointment(client):
    response = client.post("/book", data={
        "provider_id": "1",
        "customer_name": "Test User",
        "appointment_date": "2026-10-20",
        "appointment_time": "10:30",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test User" in response.data
