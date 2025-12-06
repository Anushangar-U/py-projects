from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        write_key()
        
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_password = input("Enter your master password: ")
key = load_key() 
fer = Fernet(key)

def view():
    if not os.path.exists("password.txt"):
        print("No passwords stored yet.")
        return

    with open("password.txt", "r") as file:
        for line in file.readlines():
            data = line.strip()
            if "|" in data: 
                user_name, user_password = data.split("|")
                decrypted_pass = fer.decrypt(user_password.encode()).decode()
                print(f"User: {user_name} | Password: {decrypted_pass}")

def add():
    name = input("Enter the name: ")
    pwd = input("Enter the password: ")

    with open("password.txt", "a") as file:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        file.write(f"{name}|{encrypted_pwd}\n")

while True:
    mode = input("Add a password or view a password? (add/view), q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input!!")