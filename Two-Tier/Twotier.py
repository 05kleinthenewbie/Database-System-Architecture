import mysql.connector

# Connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Default user in XAMPP
        password="",  # No password for XAMPP (change if necessary)
        database="notes_db"
    )

# Function to add a note
def add_note(title, content):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
    conn.commit()
    conn.close()
    print("✅ Note added successfully.")

# Function to view all notes
def view_notes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()

    if notes:
        print("\n📒 Your Notes:")
        for note in notes:
            print(f"🆔 ID: {note[0]} | 📌 Title: {note[1]}\n📝 {note[2]}\n" + "-"*30)
    else:
        print("⚠️ No notes found.")

# Function to update a note
def update_note(note_id, new_title, new_content):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (new_title, new_content, note_id))
    conn.commit()
    conn.close()
    print("✏️ Note updated successfully.")

# Function to delete a note
def delete_note(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    conn.commit()
    conn.close()
    print("🗑️ Note deleted successfully.")

# CLI Menu for user interaction
def main():
    while True:
        print("\n📖 MySQL Note-Taking App")
        print("1️⃣ Add Note")
        print("2️⃣ View Notes")
        print("3️⃣ Update Note")
        print("4️⃣ Delete Note")
        print("5️⃣ Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            add_note(title, content)

        elif choice == "2":
            view_notes()

        elif choice == "3":
            note_id = input("Enter note ID to update: ")
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            update_note(note_id, new_title, new_content)

        elif choice == "4":
            note_id = input("Enter note ID to delete: ")
            delete_note(note_id)

        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
