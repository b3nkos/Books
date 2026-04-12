from pathlib import Path

filename = "guest.txt"
name = input("What is your name? ")

Path(filename).write_text(name.title())
print(f"Welcome, {name.title()}! Your name has been saved.")