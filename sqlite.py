import sqlite3

def init_db():
    conn=sqlite3.connect('users.db')
    cursor=conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users (
                       athelete_id INTEGER PRIMARY KEY,
                       name TEXT,
                       refresh_token TEXT
                   )
                ''')
    conn.commit()
    conn.close()

# Enregistrer ou mettre à jour un utilisateur
def save_user(athlete_id, name, refresh_token):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT OR REPLACE INTO users (athlete_id, name, refresh_token)
                   VALUES (?,?,?)
                   ''', (athlete_id, name, refresh_token))
    conn.commit()
    conn.close()

# Récupérer un utilisateur
def get_user(athlete_id):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, refresh_token FROM users WHERE athelete_id=?', (athlete_id,))
    user = cursor.fetchone()
    conn.close()
    return user