import sqlite3

#Opens a connection to the SQLite database file
def get_db_connection():
    return sqlite3.connect('database.db')

def create_tasks_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    #Creates a task table if it dooes not exist.
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            category TEXT,
            priority REAL
            completed INTEGER DEFAULT 0 
        )
    ''')
    connection.commit() #Saves the changes to the database
    connection.close() #CLoses the connection to free up resources

def add_task(title, description, due_date, category, priority):
    connection = get_db_connection()
    cursor = connection.cursor()

    #Inserts a new task into the tasks table
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, category, priority)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, description, due_date, category, priority))

    connection.commit() #Saves the changes to the database
    connection.close() #Closes the connection to free up resources

def get_all_tasks():
    connection = get_db_connection()
    cursor = connection.cursor()

    #Retrieves all tasks from the tasks table
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()

    connection.close() #Closes the connection to free up resources
    return tasks


def mark_task_completed(task_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    #Updates the task to mark it as completed
    cursor.execute('''
        UPDATE tasks
        SET completed = 1
        WHERE id = ?
    ''', (task_id,))

    connection.commit() #Saves the changes to the database
    connection.close() #Closes the connection to free up resources

def delete_task(task_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    #Deletes the task from the tasks table
    cursor.execute('''
        DELETE FROM tasks
        WHERE id = ?
    ''', (task_id,))

    connection.commit() #Saves the changes to the database
    connection.close() #Closes the connection to free up resources

def update_task(task_id, title, description, due_date, category, priority):
    connection = get_db_connection()
    cursor = connection.cursor()

    #Updates the task details in the tasks table
    cursor.execute('''
        UPDATE tasks
        SET title = ?, description = ?, due_date = ?, category = ?, priority = ?
        WHERE id = ?
    ''', (title, description, due_date, category, priority, task_id))

def get_all_completed_tasks():
    connection = get_db_connection()
    c = connection.cursor()

    #Select tasks which are completed (Marked with 1)

    c.execte('SELECT * FROM tasks WHERE completed = 1 ORDER BY priority DESC')
    tasks = c.fetchall() #Fetches all completed tasks

    connection.close() # Closes connection

    return tasks # Returns completed tasks.



    connection.commit() #Saves the changes to the database
    connection.close() #Closes the connection to free up resources

    