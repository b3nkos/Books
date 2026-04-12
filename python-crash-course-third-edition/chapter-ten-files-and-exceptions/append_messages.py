from pathlib import Path

filename = "messages.txt"

message = ""

while True:
    response = input("Message: ")
    
    if response == "quit":
        break

    message += f"{response}\n"

Path(filename).write_text(message)
print("Messages saved. Goodbyte!")