from pathlib import Path
import json

filename = "favorite_number.json"

favorite_number = int(input("What is your favorite number? "))

content = json.dumps(favorite_number)
Path(filename).write_text(content)

print("Thanks I'll remember that.")
