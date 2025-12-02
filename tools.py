import json
import os
import getpass

USERS_FILE = "users.json"
ADMIN_PASSWORD = "admin123"  # change this

# ---------------------------
# Load Users
# ---------------------------
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

# ---------------------------
# Save Users
# ---------------------------
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ---------------------------
# Register User
# ---------------------------
def register():
    users = load_users()
    print("\n--- Register ---")

    username = input("Username: ")
    if username in users:
        print("User already exists.")
        return

    password = getpass.getpass("Password: ")
    email = input("Email (fake/optional): ")

    users[username] = {
        "password": password,
        "email": email
    }

    save_users(users)
    print("Account created!")

# ---------------------------
# Login User
# ---------------------------
def login():
    users = load_users()
    print("\n--- Login ---")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful!")
        user_menu(username)
    else:
        print("Invalid credentials.")

# ---------------------------
# Admin Panel
# ---------------------------
def admin_panel():
    print("\n--- Admin Panel ---")
    pwd = getpass.getpass("Admin Password: ")

    if pwd != ADMIN_PASSWORD:
        print("Wrong admin password.")
        return

    users = load_users()

    print("\nUsers List:")
    for user, data in users.items():
        print(f"- {user} | email: {data['email']} | pass: {data['password']}")

# ---------------------------
# Forgot Password
# ---------------------------
def forgot_password():
    users = load_users()
    print("\n--- Password Recovery ---")
    username = input("Username: ")

    if username in users:
        print(f"Password: {users[username]['password']}")
    else:
        print("User not found.")

# ---------------------------
# User Menu (Tools)
# ---------------------------
def user_menu(username):
    while True:
        print(f"""
======== ToolBox ========
Logged in as: {username}

1 - Network Scan (dummy)
2 - Device Info (dummy)
3 - Logout
""")
        choice = input("Choose: ")

        if choice == "1":
            print("Scanning network... (simulation)")
        elif choice == "2":
            print("Device: Android (simulated)")
        elif choice == "3":
            break
        else:
            print("Invalid option.")

# ---------------------------
# Main Menu
# ---------------------------
def main():
    while True:
        print("""
=========================
    Login System v1
=========================

1 - Register
2 - Login
3 - Forgot Password
4 - Admin Panel
0 - Exit
""")
        choice = input("Choose: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            admin_panel()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

main()
