from contacts import contacts
from utils import add_contact, show_contacts, find_contact

active = True

print("📇 Contact Manager")

while active:
    print("\n1. Add contact")
    print("2. Show contacts")
    print("3. Find contact")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "4":
        print("Goodbye! 🤗")
        active = False
    elif choice == "1":
        add_contact(contacts)
    elif choice == "2":
        show_contacts(contacts)
    elif choice == "3":
        find_contact(contacts)