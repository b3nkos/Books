from pathlib import Path
import json

FILENAME = "notes_storage.json"

class NotesApp:
    def __init__(self):
        self.path = Path(FILENAME)
        self.notes = self.load_notes()

    def load_notes(self) -> list:
        """Load notes from file or return empty list"""
        notes = []

        if not self.path.exists():
            notes

        try:
            notes = json.loads(self.path.read_text())
        except FileNotFoundError:
            return notes
        else:
            return notes
        
    def save_notes(self):
        """Save notes to file"""
        self.path.write_text(json.dumps(self.notes))

    def add_note(self):
        """Ask user for note text and save it"""
        note = input("Write the note: ")
        self.notes.append(note.title())
        self.save_notes()
    
    def show_notes(self):
        """Display all notes"""
        if not self.notes:
            print("There are not notes yet!")
        else:
            print("\nList of notes:")
            for index, note in enumerate(self.load_notes()):
                print(f"{index}: {note}")
    
    def delete_note(self):
        """Remove a note by index"""
        if not self.notes:
            print("There are not notes yet!")
        else:
            self.show_notes()

            while True:
                try:
                    index = int(input("Which note do you want to remove, write a number?: "))
                except ValueError:
                    pass
                else:
                    try:
                        note = self.notes.pop(index)
                    except IndexError:
                        print("Invalid number choose other")
                    else:
                        self.save_notes()
                        print(f"The note \"{note}\" was removed")
                        break
    
    def run(self):
        while True:
            print("\n1. Add note")
            print("2. Show notes")
            print("3. Delete note")
            print("4. Quit\n")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.show_notes()
            elif choice == "3":
                self.delete_note()
            elif choice == "4":
                print("Goodbyte!")
                break
            else:
                print("Invalid option.")


app = NotesApp()
app.run()