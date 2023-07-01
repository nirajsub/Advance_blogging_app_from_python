import sqlite3

def create_post(title, content, user_id):
    conn = sqlite3.connect('blogging.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)', (title, content, user_id))
    conn.commit()
    conn.close()

# def get_all_posts():
#     conn = sqlite3.connect('blogging.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT posts.id, title, content, username, timestamp FROM posts INNER JOIN users ON posts.user_id = users.id ORDER BY timestamp DESC')
#     posts = cursor.fetchall()
#     conn.close()
#     return posts
def get_all_posts():
    conn = sqlite3.connect('blogging.db')
    cursor = conn.cursor()
    cursor.execute('SELECT posts.id, title, content, users.username, timestamp FROM posts INNER JOIN users ON posts.user_id = users.id ORDER BY timestamp DESC')
    posts = cursor.fetchall()
    conn.close()
    return posts



def get_single_posts(post_id):
    conn = sqlite3.connect('blogging.db')
    cursor = conn.cursor()
    cursor.execute('SELECT posts.id, title, content, username, timestamp FROM posts INNER JOIN users on posts.user_id = users.id WHERE post_id=?', (post_id,))
    post = cursor.fetchone()
    conn.close()
    return post

def update_post(post_id, title, content):
    conn = sqlite3.connect('blogging.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE posts SET title=?, content=? WHERE id=?', (title, content, post_id))
    conn.commit()
    conn.close()

def delete_post(post_id):
    conn = sqlite3.connect('blogging.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM posts WHERE id=?', (post_id,))
    conn.commit()
    conn.close()

def create_comment(post_id, user_id, content):
    conn = sqlite3.connect('blogging.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comments (post_id, user_id, content) VALUES (?, ?, ?)', (post_id, user_id, content))
    conn.commit()
    conn.close()

def get_comments_for_post(post_id):
    conn = sqlite3.connect('blogging.db')
    cursor = conn.cursor()
    cursor.execute('SELECT comments.id, content, username, timestamp FROM comments INNER JOIN users ON comments.user_id = users.id WHERE post_id=?', (post_id,))
    comments = cursor.fetchall()
    conn.close()
    return comments
