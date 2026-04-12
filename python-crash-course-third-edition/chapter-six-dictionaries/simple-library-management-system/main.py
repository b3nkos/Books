from data import library
from library import show_books, borrow_book

print("📚 Library System\n")
show_books(library)

print("\nBorrowing books:\n")

borrow_book(library, "Dune")
borrow_book(library, "1984")

print("\nUpdated library:\n")
show_books(library)