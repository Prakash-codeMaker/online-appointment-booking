import os
import tempfile

import pytest

import database


@pytest.fixture()
def client(monkeypatch):
    db_file = tempfile.NamedTemporaryFile(delete=False)
    db_file.close()

    monkeypatch.setattr(database, "DB_PATH", database.Path(db_file.name))

    import app as app_module

    database.init_db()
    app_module.app.config.update(TESTING=True)

    with app_module.app.test_client() as client:
        yield client

    os.unlink(db_file.name)


def test_homepage_lists_providers(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Dr. Asha Mehta" in response.data


def test_provider_search(client):
    response = client.get("/?q=physio")
    assert response.status_code == 200
    assert b"Rahul Verma" in response.data
    assert b"Dr. Asha Mehta" not in response.data


def test_book_appointment(client):
    response = client.post("/book", data={
        "provider_id": "1",
        "customer_name": "Test User",
        "appointment_date": "2026-10-20",
        "appointment_time": "10:30",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Test User" in response.data


def test_double_booking_is_rejected(client):
    payload = {
        "provider_id": "1",
        "customer_name": "First User",
        "appointment_date": "2026-10-21",
        "appointment_time": "11:00",
    }

    first = client.post("/book", data=payload, follow_redirects=True)
    assert b"First User" in first.data

    second_payload = dict(payload)
    second_payload["customer_name"] = "Second User"
    second = client.post("/book", data=second_payload, follow_redirects=True)

    assert b"already booked" in second.data


def test_cancel_appointment(client):
    client.post("/book", data={
        "provider_id": "2",
        "customer_name": "Cancel User",
        "appointment_date": "2026-10-22",
        "appointment_time": "09:30",
    })

    response = client.post("/appointments/1/cancel", follow_redirects=True)
    assert response.status_code == 200
    assert b"Cancelled" in response.data


def test_reschedule_appointment(client):
    client.post("/book", data={
        "provider_id": "3",
        "customer_name": "Reschedule User",
        "appointment_date": "2026-10-23",
        "appointment_time": "14:00",
    })

    response = client.post("/appointments/1/reschedule", data={
        "appointment_date": "2026-10-24",
        "appointment_time": "15:30",
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"2026-10-24" in response.data
    assert b"15:30" in response.data
