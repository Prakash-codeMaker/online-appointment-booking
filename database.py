import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("appointments.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS providers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    service TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    appointment_date TEXT NOT NULL,
    appointment_time TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Booked',
    FOREIGN KEY(provider_id) REFERENCES providers(id)
);
"""

def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    db.executescript(SCHEMA)
    count = db.execute("SELECT COUNT(*) FROM providers").fetchone()[0]
    if count == 0:
        db.executemany(
            "INSERT INTO providers (name, service, description) VALUES (?, ?, ?)",
            [
                ("Dr. Asha Mehta", "General Consultation", "Routine consultation and health guidance."),
                ("Rahul Verma", "Physiotherapy", "Mobility, recovery and physiotherapy sessions."),
                ("Ananya Shah", "Dental Consultation", "Routine dental check-up and consultation."),
            ],
        )
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
