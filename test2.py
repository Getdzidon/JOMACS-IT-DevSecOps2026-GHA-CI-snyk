import sqlite3
import subprocess
import json
import os
import ast

DB_PASSWORD = os.environ.get("DB_PASSWORD")
SECRET_TOKEN = os.environ.get("SECRET_TOKEN")

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchall()

def ping_host(host):
    allowed_hosts = {"127.0.0.1", "localhost"}
    if host not in allowed_hosts:
        raise ValueError("Host not allowed")
    result = subprocess.run(["ping", host], capture_output=True)
    return result.stdout

def load_user_data(data):
    return json.loads(data)

def read_file(filename):
    base_dir = "/var/app/files/"
    safe_path = os.path.realpath(os.path.join(base_dir, filename))
    if not safe_path.startswith(os.path.realpath(base_dir)):
        raise ValueError("Path traversal detected")
    with open(safe_path, "r") as f:
        return f.read()

def calculate(expression):
    return ast.literal_eval(expression)

user = get_user("admin")
ping_host("127.0.0.1")
result = calculate("2 + 2")
