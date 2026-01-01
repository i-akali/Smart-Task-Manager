import sqlite3

#Opens a connection to the SQLite database file
def get_db_connection():
    return sqlite3.connect('database.db')

def create_create_tasks_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    #Creates a task table if it dooes not exist.
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT,
            status TEXT NOT NULL,
            due_date TEXT
        )
    ''')
    connection.commit()
    connection.close()