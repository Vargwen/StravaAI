import requests

def get_activities(access_token, limit = 5):
    """Récupère les 5 dernières activités."""
    url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'per_page': 20}

    response = requests.get(url, headers=headers, params=params).json()
    running_activities = [act for act in response if act['type'] == 'Run']

    return running_activities[:limit]