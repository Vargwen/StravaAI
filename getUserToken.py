import requests
import os
from dotenv import load_dotenv
from sqlite import save_user, get_user
import db

# 1. Chargement des tokens
load_dotenv()
CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")

def get_token(code):    
    url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    }
    
    response = requests.post(url, data=payload)
    data = response.json()
    
    # Extraction des données utiles
    user_id = data['athlete']['id']
    refresh_token = data['refresh_token']
    access_token = data['access_token']
    name = data['athlete']['firstname']

    # Sauvegarde de l'utilisateur dans supabase
    db.save_user(user_id, name, refresh_token)

    return user_id, refresh_token

def get_user_token(user_id):
    """Récupère le token de l'utilisateur via sqlite."""
    
    user_data = db.get_user(user_id)

    if not user_data:
        raise Exception("Utilisateur non trouvé en base de données.")
    
    name, refresh_token = user_data

    url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }

    response = requests.post(url, data=payload)
    
    if response.status_code != 200:
        raise Exception(f"Erreur Strava : {response.text}")
        
    response_data = response.json()

    new_refresh_token = response_data['refresh_token']
    db.save_user(user_id, name, new_refresh_token)

    return response_data['access_token']