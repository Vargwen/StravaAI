import sqlite3

def init_db():
    conn=sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users (
                       athlete_id INTEGER PRIMARY KEY,
                       name TEXT,
                       refresh_token TEXT
                   )
                ''')
    conn.commit()
    conn.close()

init_db()

# Enregistrer ou mettre à jour un utilisateur
def save_user(athlete_id, name, refresh_token):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT OR REPLACE INTO users (athlete_id, name, refresh_token)
                   VALUES (?,?,?)
                   ''', (athlete_id, name, refresh_token))
    conn.commit()
    conn.close()

# Récupérer un utilisateur
def get_user(athlete_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, refresh_token FROM users WHERE athlete_id=?', (athlete_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT athlete_id, name FROM users')
    rows = cursor.fetchall()
    conn.close()
    return {row[1]: row[0] for row in rows}