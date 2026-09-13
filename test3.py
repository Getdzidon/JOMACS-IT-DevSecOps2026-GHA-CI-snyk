import os
import sqlite3
import subprocess
from flask import Flask, request, abort

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

@app.route("/user", methods=["GET"])
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return str(cursor.fetchall())

@app.route("/cmd", methods=["POST"])
def execute_command():
    allowed_commands = {"uptime", "date", "whoami"}
    user_input = request.form.get("cmd")
    if user_input not in allowed_commands:
        abort(400, "Command not allowed")
    result = subprocess.run([user_input], capture_output=True)
    return result.stdout.decode()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
