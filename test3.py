import os
import sqlite3
import subprocess
from flask import Flask, request, abort, jsonify
from markupsafe import escape

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

COMMAND_MAP = {
    "uptime": ["uptime"],
    "date": ["date"],
    "whoami": ["whoami"],
}

@app.route("/user", methods=["GET"])
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route("/cmd", methods=["POST"])
def execute_command():
    user_input = request.form.get("cmd")
    command = COMMAND_MAP.get(user_input)
    if command is None:
        abort(400, "Command not allowed")
    result = subprocess.run(command, capture_output=True)
    return jsonify({"output": escape(result.stdout.decode())})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
