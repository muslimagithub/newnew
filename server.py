from flask import Flask, request, jsonify, send_from_directory
import sqlite3
from datetime import datetime

app = Flask(__name__, static_folder='static')

def check_registration(code):
    student_id = code.split(',')[0].split(':')[1].strip()
    today = datetime.now().date()
    
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT registration_date FROM students WHERE id=?", (student_id,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        registration_date = datetime.strptime(result[0], "%Y-%m-%d").date()
        return registration_date == today
    return False

# This route will serve your 'index.html' file
@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/check_registration', methods=['POST'])
def check_registration_route():
    data = request.get_json()
    code = data.get('code')
    registered_today = check_registration(code)
    return jsonify({'registeredToday': registered_today})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
