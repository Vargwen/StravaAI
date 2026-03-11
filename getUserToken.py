import requests
import json
import os
from dotenv import load_dotenv

# 1. Chargement des tokens
load_dotenv()
CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
TOKEN_FILE = "user.json"

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

    # On stocke le token dans un fichier JSON
    users ={}
    if os.path.exists(TOKEN_FILE) and os.path.getsize(TOKEN_FILE) > 0:
        with open(TOKEN_FILE, 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                print("Le fichier était corrompu, réinitialisation.")

    # On ajoute le nouvel utilisateur
    users[str(user_id)] = {
        'name': name,
        'refresh_token': refresh_token
    }

    # On sauvegarde tout
    with open(TOKEN_FILE, 'w') as f:
        json.dump(users, f, indent=4)

    return user_id, refresh_token

def get_user_token(user_id):
    """Récupère le token de l'utilisateur à partir du fichier JSON."""
    if not os.path.exists(TOKEN_FILE):
        raise Exception("Le fichier de token n'existe pas. Veuillez vous connecter via l'application.")
    
    with open(TOKEN_FILE, 'r') as f:
        users = json.load(f)
    
    refresh_token = users[str(user_id)]['refresh_token']

    url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }

    response = requests.post(url, data=payload)
    response_data = response.json()

    users[str(user_id)]['refresh_token'] = response_data['refresh_token']

    with open(TOKEN_FILE, 'w') as f:
        json.dump(users, f, indent=4)

    return response_data['access_token']