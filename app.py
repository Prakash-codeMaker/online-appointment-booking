from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, get_db

app = Flask(__name__)
app.config["SECRET_KEY"] = "agile-appointment-demo"

init_db()

@app.get("/")
def index():
    query = request.args.get("q", "").strip()
    db = get_db()
    if query:
        providers = db.execute(
            """SELECT id, name, service, description FROM providers
               WHERE name LIKE ? OR service LIKE ? OR description LIKE ?
               ORDER BY name""",
            (f"%{query}%", f"%{query}%", f"%{query}%"),
        ).fetchall()
    else:
        providers = db.execute(
            "SELECT id, name, service, description FROM providers ORDER BY name"
        ).fetchall()
    return render_template("index.html", providers=providers, query=query)

@app.post("/book")
def book():
    provider_id = request.form.get("provider_id", type=int)
    customer_name = request.form.get("customer_name", "").strip()
    appointment_date = request.form.get("appointment_date", "").strip()
    appointment_time = request.form.get("appointment_time", "").strip()

    if not all([provider_id, customer_name, appointment_date, appointment_time]):
        flash("Please complete all booking fields.")
        return redirect(url_for("index"))

    db = get_db()
    provider = db.execute("SELECT id, name FROM providers WHERE id = ?", (provider_id,)).fetchone()
    if provider is None:
        flash("Provider not found.")
        return redirect(url_for("index"))

    existing = db.execute(
        """SELECT id FROM appointments
           WHERE provider_id = ? AND appointment_date = ? AND appointment_time = ?
           AND status = 'Booked'""",
        (provider_id, appointment_date, appointment_time),
    ).fetchone()

    if existing:
        flash("That time slot is already booked.")
        return redirect(url_for("index"))

    db.execute(
        """INSERT INTO appointments
           (provider_id, customer_name, appointment_date, appointment_time, status)
           VALUES (?, ?, ?, ?, 'Booked')""",
        (provider_id, customer_name, appointment_date, appointment_time),
    )
    db.commit()
    flash("Appointment booked successfully.")
    return redirect(url_for("appointments"))

@app.get("/appointments")
def appointments():
    db = get_db()
    rows = db.execute(
        """SELECT appointments.id, appointments.customer_name,
                  appointments.appointment_date, appointments.appointment_time,
                  appointments.status, providers.name AS provider_name,
                  providers.service
           FROM appointments
           JOIN providers ON providers.id = appointments.provider_id
           ORDER BY appointment_date, appointment_time"""
    ).fetchall()
    return render_template("appointments.html", appointments=rows)

@app.post("/appointments/<int:appointment_id>/cancel")
def cancel(appointment_id):
    db = get_db()
    db.execute(
        "UPDATE appointments SET status = 'Cancelled' WHERE id = ?",
        (appointment_id,),
    )
    db.commit()
    flash("Appointment cancelled.")
    return redirect(url_for("appointments"))

if __name__ == "__main__":
    app.run(debug=True)
