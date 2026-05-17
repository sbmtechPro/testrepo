# vulnerable_app.py
from flask import Flask, request, render_template_string, redirect
import sqlite3

app = Flask(__name__)

def db():
    conn = sqlite3.connect("test.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin123')")
    conn.execute("INSERT OR IGNORE INTO users VALUES (2, 'bob', 'password')")
    conn.commit()
    return conn

@app.route("/")
def index():
    return """
    <h2>Vulnerable Test App</h2>
    <a href="/login">SQL Injection Test</a><br>
    <a href="/change-password">CSRF Test</a>
    """

# -------------------------
# SQL INJECTION VULNERABLE
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = db()

        # VULNERABLE: string concatenation in SQL
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

        rows = conn.execute(query).fetchall()

        if rows:
            return f"Logged in as {rows[0][1]}<br><pre>{query}</pre>"
        else:
            return f"Login failed<br><pre>{query}</pre>"

    return """
    <h3>Login</h3>
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <button type="submit">Login</button>
    </form>
    """
# -------------------------
@app.route("/change-password", methods=["GET", "POST"])
def change_password():
    if request.method == "POST":
        new_password = request.form["new_password"]

        conn = db()
        conn.execute(f"UPDATE users SET password = '{new_password}' WHERE username = 'admin'")
        conn.commit()

        return f"Admin password changed to: {new_password}"

    return """
    <h3>Change Admin Password</h3>
    <form method="POST">
        New password: <input name="new_password">
        <button type="submit">Change</button>
    </form>
    """

if __name__ == "__main__":
    db()
    app.run(debug=True, port=5000)
