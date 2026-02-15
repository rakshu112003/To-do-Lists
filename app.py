from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rakshitha123",   # your password
            database="todo_app"        # your existing DB
        )
        return conn
    except:
        return None

@app.route('/')
def home():
    return "Backend is running! Go to /todos to see tasks."

@app.route('/todos', methods=['GET'])
def todos():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM todos")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            if rows:  # DB has tasks → use them
                return jsonify(rows)
        except:
            pass
    # Fallback → minimal meaningful tasks
    tasks = [
        {"id": 1, "task": "Simple Task", "completed": False},
        {"id": 2, "task": "MERN Stack Project Completed", "completed": True},
        {"id": 3, "task": "Python Project Finished", "completed": True},
        {"id": 4, "task": "Write Report", "completed": False}
    ]
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)