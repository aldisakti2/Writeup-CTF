from hashlib import sha256
from flask import Flask, redirect, request, g
import os
import sqlite3

FLAG = "COMPFEST16{FLAG}"
SECRET = os.getenv("SECRET") or "epicsecret"
app = Flask(__name__)


def init():
    db = sqlite3.connect("/tmp/app.db")
    db.execute(
        """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        is_admin INT DEFAULT 0 NOT NULL
        );"""
    )

    # DO NOT SAVE PLAINTEXT PASSWORD IN REAL LIFE!!!!!!!!!!!!!!!!!!
    # Use hashing and salting to save password
    db.execute(
        """INSERT OR IGNORE INTO users(id, username, password, is_admin) VALUES
            (1, 'rorre', 'meow', 0),
            (2, 'meervix', 'toksik', 0);
            """
    )
    db.commit()


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("/tmp/app.db")
    return db


def query(sql: str, params: list[object] | None = None):
    cur = get_db().cursor()
    if not params:
        params = []

    results = []
    for s in sql.split(";"):
        cur.execute(s, params)
        results.append(cur.fetchall())

    get_db().commit()
    return results


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def create_hash(value: str):
    return sha256((value + SECRET).encode()).hexdigest()


def parse_cookie(value: str):
    try:
        value, hash = value.split("-")
        if create_hash(value) != hash:
            return False, None
        return True, value
    except:
        return False, None


@app.get("/")
def index():
    valid, user = parse_cookie(request.cookies.get("user_id", ""))
    if not valid:
        user = "Guest"

    bottom = "<a href='/login'>Login</a>"
    if user != "Guest":
        row = query("SELECT username, is_admin FROM users WHERE id = ?", [user])[0]
        if row:
            user = row[0][0]
            bottom = "<a href='/logout'>Logout</a>"
            if row[0][1] == 1:
                bottom += f"<p>Flag: {FLAG}</p>"
        else:
            user = "Guest"

    return f"<p>Hello, {user}.</p>{bottom}"


@app.get("/logout")
def logout():
    resp = redirect("/")
    resp.delete_cookie("user_id")
    return resp


@app.get("/login")
def login():
    return """
<form method="POST">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>
    
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password"><br><br>
    
    <input type="submit" value="Submit">
</form>
"""


@app.post("/login")
def process_login():
    username = request.form.get("username")
    password = request.form.get("password")
    if not all([username, password]):
        return redirect("/login")

    row = query(f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'")[0]
    if not row:
        return redirect("/login")

    resp = redirect("/")
    resp.set_cookie("user_id", str(row[0][0]) + "-" + create_hash(str(row[0][0])))
    return resp


if __name__ == "__main__":
    init()
    app.run()
