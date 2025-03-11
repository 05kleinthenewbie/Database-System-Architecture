import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a note
def add_note(title, content):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()
    print("✅ Note added successfully.")

# Function to view all notes
def view_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()

    if notes:
        print("\n📒 Your Notes:")
        for note in notes:
            print(f"🆔 ID: {note[0]}\n📌 Title: {note[1]}\n📝 Content: {note[2]}\n" + "-"*30)
    else:
        print("⚠️ No notes found.")

# Function to delete a note
def delete_note(note_id):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    print("🗑️ Note deleted successfully.")

# CLI Menu for interaction
def main():
    init_db()
    while True:
        print("\n📖 Simple Note-Taking App")
        print("1️⃣ Add Note")
        print("2️⃣ View Notes")
        print("3️⃣ Delete Note")
        print("4️⃣ Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            add_note(title, content)

        elif choice == "2":
            view_notes()

        elif choice == "3":
            note_id = input("Enter note ID to delete: ")
            if note_id.isdigit():
                delete_note(int(note_id))
            else:
                print("⚠️ Invalid ID. Please enter a number.")

        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
