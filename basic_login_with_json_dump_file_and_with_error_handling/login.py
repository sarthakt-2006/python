import json

username = {}

try:
    with open("username.json", "r") as username_file:
        username = json.load(username_file)
except FileNotFoundError:
    pass

if username:
    print(f"Welcome back, {username['first_name']} {username['last_name']}!")
else:
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    username = {"first_name": first_name, "last_name": last_name}
    with open("username.json", "w") as username_file:
        json.dump(username, username_file)