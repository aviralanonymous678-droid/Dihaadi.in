import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATABASE = 'registrations.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "Welcome to Dihaadi.in Backend"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO registrations (role, name, aadhaar, mobile, skills, availability) VALUES (?, ?, ?, ?, ?, ?)',
        (data['role'], data['name'], data['aadhaar'], data['mobile'], data.get('skills', ''), data.get('availability', ''))
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Registration successful!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
