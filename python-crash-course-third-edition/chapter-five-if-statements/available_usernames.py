current_users = ["jose", "maria", "admin", "luis"]
new_users = ["jose", "andres", "Admin", "carla"]

for user in new_users:
    if user.lower() in current_users:
        print(f"Sorry, {user} is already taken")
    else:
        print(f"{user.title()} is available")