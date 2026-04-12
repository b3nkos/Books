users = {
    "jose": {
        "first": "Jose",
        "last": "Martinez",
        "location": "Colombia"
    },
    "maria": {
        "first": "Maria",
        "last": "Gomez",
        "location": "Spain"
    }
}

for user_name, information in users.items():
    print(f"Username: {user_name}\nFull name: {information["first"]} {information["last"]}\nLocation: {information["location"]}\n")