import sqlite3

def create_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            registration_date DATE
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
