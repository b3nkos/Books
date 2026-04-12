from pathlib import Path
import json

filename = "favorite_number.json"
path = Path(filename)

if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know yor favorite number! It's {favorite_number}")
else:
    favorite_number = int(input("What is your favorite number? "))

    content = json.dumps(favorite_number)
    path.write_text(content)
    print("Thanks I'll remember that.")