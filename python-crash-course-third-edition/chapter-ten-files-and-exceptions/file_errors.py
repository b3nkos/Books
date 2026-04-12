from pathlib import Path

filename = "missing_file.txt"

try:
    Path(filename).read_text()
except FileNotFoundError:
    print("Sorry, the file does not exist")
else:
    print("The file is readed correctly")