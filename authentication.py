import sqlite3

conn = sqlite3.connect('blogging.db')
cursor = conn.cursor()
def create_user(username, password, fullname, email, phone, bio):
    cursor.execute('INSERT INTO users (username, password, fullname, email, phone, bio) VALUES (?, ?, ?, ?, ?, ?)', (username, password, fullname, email, phone, bio))
    conn.commit()

def authenticate_user(username, password):
    cursor.execute('SELECT id FROM users WHERE username=? AND password=?', (username, password))
    result = cursor.fetchone()
    return result is not None

def get_user_by_id(user_id):
    cursor.execute('SELECT id, username, fullname, email, phone, bio  FROM users WHERE id=?', (user_id,))
    user = cursor.fetchone()
    return user

def get_user_by_username(username):
    cursor.execute('SELECT id, username, fullname, email, phone, bio FROM users WHERE username=?', (username,))
    user = cursor.fetchone()
    return user

