

import json
import datetime

notes = []

def save_notes():
    with open(".venv/notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    global notes
    try:
        with open(".venv/notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def add_note(title, message):
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    save_notes()
    print("Note successfully added.")

def edit_note(note_id, title, message):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["message"] = message
            note["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Note successfully edited.")
            return
    print("Note not found.")

def delete_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes()
            print("Note successfully deleted.")
            return
    print("Note not found.")

def read_notes(date_filter=None):
    for note in notes:
        if date_filter:
            if note["created_at"].split()[0] == date_filter or note["updated_at"].split()[0] == date_filter:
                print(f"ID: {note['id']}\nTitle: {note['title']}\nMessage: {note['message']}\nCreated at: {note['created_at']}\nUpdated at: {note['updated_at']}")
        else:
            print(f"ID: {note['id']}\nTitle: {note['title']}\nMessage: {note['message']}\nCreated at: {note['created_at']}\nUpdated at: {note['updated_at']}")

# Load notes from file
load_notes()

while True:
    command = input("Enter command (add, edit, delete, read): ").lower()

    if command == "add":
        title = input("Enter note title: ")
        message = input("Enter note message: ")
        add_note(title, message)
    elif command == "edit":
        note_id = int(input("Enter note ID to edit: "))
        title = input("Enter new note title: ")
        message = input("Enter new note message: ")
        edit_note(note_id, title, message)
    elif command == "delete":
        note_id = int(input("Enter note ID to delete: "))
        delete_note(note_id)
    elif command == "read":
        date_filter = input("Enter date filter (YYYY-MM-DD) or leave empty for all notes: ")
        read_notes(date_filter)
    else:
        print("Invalid command. Please try again.")
