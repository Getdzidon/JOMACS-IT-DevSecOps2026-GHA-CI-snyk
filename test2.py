import sqlite3
import subprocess
import pickle
import os

# Hardcoded credentials
DB_PASSWORD = "supersecretpassword123"
SECRET_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ123456"

# SQL Injection vulnerability
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# Command Injection vulnerability
def ping_host(host):
    result = subprocess.run("ping " + host, shell=True, capture_output=True)
    return result.stdout

# Insecure deserialization vulnerability
def load_user_data(data):
    return pickle.loads(data)

# Path traversal vulnerability
def read_file(filename):
    base_dir = "/var/app/files/"
    with open(base_dir + filename, "r") as f:
        return f.read()

# Insecure use of eval
def calculate(expression):
    return eval(expression)

user = get_user("admin")
ping_host("127.0.0.1")
result = calculate("2 + 2")
