import json
import os
import hashlib
from time import sleep

DATABASE = "database.json"


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def load_db():
    if not os.path.exists(DATABASE):
        with open(DATABASE, "w") as f:
            json.dump({"users": {}, "admin": {}}, f, indent=4)

    with open(DATABASE, "r") as f:
        return json.load(f)


def save_db(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)


def register_user():
    data = load_db()

    print("\n[ REGISTER ]")
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")

    if username in data["users"]:
        print("User already exists.")
        return False

    hashed = hash_password(password)
    data["users"][username] = {"email": email, "password": hashed}

    save_db(data)
    print("Registration complete.")
    sleep(1)
    return True


def login_user():
    data = load_db()

    print("\n[ LOGIN ]")
    username = input("Username: ")
    password = input("Password: ")

    hashed = hash_password(password)

    # admin login
    if username == "admin":
        if "password" not in data["admin"] or data["admin"]["password"] == "":
            print("No admin exists. Creating new admin...")
            data["admin"]["password"] = hashed
            save_db(data)
            print("Admin created. Login again.")
            return False

        if hashed == data["admin"]["password"]:
            print("Admin access granted.")
            return "admin"
        else:
            print("Wrong admin password.")
            return False

    # user login
    if username not in data["users"]:
        print("User not found.")
        return False

    if hashed == data["users"][username]["password"]:
        print("Login successful.")
        return username

    print("Wrong password.")
    return False
