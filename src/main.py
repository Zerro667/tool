import os
import time
from login import login_user, register_user

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def load_banner():
    with open("src/banner.txt", "r") as f:
        print(f.read())

def matrix_effect():
    for _ in range(40):
        print("01 10 01 10 01 10 01 10 01 10 01 10")
        time.sleep(0.02)

def menu(username):
    clear()
    load_banner()
    print(f"\nLogged in as: {username}\n")

    print("1) Phone Number Scanner")
    print("2) Instagram OSINT")
    print("3) Exit")

    choice = input("\nSelect: ")
    return choice


def main():
    clear()
    matrix_effect()
    load_banner()

    print("1) Login")
    print("2) Register")
    print("3) Exit")

    option = input("\nChoose: ")

    if option == "1":
        user = login_user()
        if user:
            choice = menu(user)
    elif option == "2":
        register_user()
    else:
        exit()

main()
