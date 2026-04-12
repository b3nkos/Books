from users import users, login_attempts
from permissions import ADMIN_ACTIONS
from report import show_report

print("🔐 User Access System\n")

def greet_users(users):
    for user in users:
        if user.lower() == "admin":
            print(f"Welcome {user}! You have full access.")
        else:
            print(f"Welcome {user}!")

def print_admin_permissions(permissions):
    for permission in permissions:
        print(f"- {permission}")


greet_users(users)
print("\nAdmin permissions:")
print_admin_permissions(ADMIN_ACTIONS)
print("\nLogin report:")
show_report(users, login_attempts)
print("\nSystem check completed.")