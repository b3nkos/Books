def show_books(library):
    for book, information in library.items():
        if information["copies"] > 0:
            print(f"{book} by {information["author"]} - Available ({information["copies"]} copies)")
        else:
            print(f"{book} by {information["author"]} - Not available")

def borrow_book(library, title):
    if library.get(title)["copies"] > 0:
        library.get(title)["copies"] -= 1
        print(f"You borrowed {title} successfully!")
    else:
        print(f"Sorry, {title} is not available right now.")