users = ["admin", "jose", "maria", "luis"]

for user in users:
    if user == "admin":
        print(f"Hello {user}, would you like to see the system status?")
    else:
        print(f"Hello {user.title()}, thank you for loggin in again")