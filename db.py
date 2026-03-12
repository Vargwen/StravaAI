import os
import psycopg2
import streamlit as st

# Fonction pour créer la connexion à Supabase
def get_db_connection():
    # L'URL est récupérée depuis les Secrets de Streamlit
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def save_user(athlete_id, name, refresh_token):
    """Insère ou met à jour un utilisateur dans la base."""
    conn = get_db_connection()
    cur = conn.cursor()
    # Utilisation de %s pour éviter les injections SQL
    cur.execute("""
        INSERT INTO users (athlete_id, name, refresh_token)
        VALUES (%s, %s, %s)
        ON CONFLICT (athlete_id) 
        DO UPDATE SET refresh_token = EXCLUDED.refresh_token, name = EXCLUDED.name
    """, (athlete_id, name, refresh_token))
    conn.commit()
    cur.close()
    conn.close()

def get_user(athlete_id):
    """Récupère les infos d'un utilisateur spécifique."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, refresh_token FROM users WHERE athlete_id = %s", (athlete_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def get_all_users():
    """Récupère la liste complète des utilisateurs."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT athlete_id, name, refresh_token FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows