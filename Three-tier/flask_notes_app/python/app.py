from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Allows frontend access

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Change to your MySQL username
    password="",  # Change to your MySQL password
    database="notes3_db"
)
cursor = db.cursor()

# API Route: Get all notes
@app.route("/notes", methods=["GET"])
def get_notes():
    cursor.execute("SELECT * FROM T3")
    notes = cursor.fetchall()
    return jsonify([{"id": note[0], "title": note[1], "content": note[2], "created_at": note[3]} for note in notes])

# API Route: Add a new note
@app.route("/notes", methods=["POST"])
def add_note():
    data = request.json
    cursor.execute("INSERT INTO T3 (title, content) VALUES (%s, %s)", (data["title"], data["content"]))
    db.commit()
    return jsonify({"message": "Note added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
