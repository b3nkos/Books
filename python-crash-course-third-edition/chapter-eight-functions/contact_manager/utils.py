def add_contact(contacts):
    """Add a new contact into the agenda"""
    name = input("What is the contact's name? ")
    phone = input("What is the contact's phone? ")
    contacts[phone] = name

def show_contacts(contacts):
    """Print the list of saved contacts"""
    if contacts:
        for phone, name in contacts.items():
            print(f"Name: {name.title()}\nPhone: {phone}\n")
    else:
        print("There are not contacts yet!")

def find_contact(contacts):
    """Find a contact by name"""
    name_to_find = input("What is the contact's name? ")
    is_found = False

    for phone, name in contacts.items():
        if name.title() == name_to_find.title():
            print(f"Name: {name.title()}\nPhone: {phone}")
            is_found = True
            break

    if not is_found:
        print(f"Contact \'{name_to_find}\' not found")