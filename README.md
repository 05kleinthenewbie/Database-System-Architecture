 Notes Management Applications

This repository contains three different implementations of a notes management system:
Single-Tier (SQLite-based standalone script)
Two-Tier (MySQL database with Python backend)
Three-Tier (Flask-based web application with database and frontend)


 1. Single-Tier Application
 Overview
- A simple Python script that stores notes in an SQLite database.
- Allows adding notes via a command-line interface.

 How to Run
1. Ensure you have **Python 3.x** installed.
2. Run the script:
   ```sh
   python single-tier.py
   
 2. Two-Tier Application
 Overview
- Uses a **MySQL database** for storing notes.
- A Python script connects to the database to insert and retrieve notes.

 How to Run
1. Install MySQL and create a database named `notes_db`.
2. Import the `notes_db.sql` file into MySQL.
3. Run the script:
   ```sh
   python Twotier.py
   
 3. Three-Tier Application
 Overview
- A **Flask-based web application** with a frontend, backend, and database.
- Allows users to interact with notes through a web interface.

 How to Run
1. Install Flask:
   ```sh
   pip install flask
   ```
2. Navigate to the `flask_notes_app` directory.
3. Run the Flask application:
   ```sh
   python app.py
   ```
4. Open a browser and go to `http://localhost:5000` to access the app.

 Contributing
Feel free to modify the code and submit pull requests!

 License
This project is open-source. Modify and use it as needed!

GROUP 4

Princess Ong                                                                                                                                                                  
Rachelle Pateño                                                                                                                                                               Klein Thon Racasa

