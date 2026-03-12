from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_KEY")

def analyze_with_gemini(activities_data):
    """Envoie les activités à Gemini pour une analyse."""
    client = genai.Client(api_key=GEMINI_API_KEY)
    # Formatage simple des données pour économiser les tokens
    summary = [{"name": a['name'], "distance": a['distance'], "time": a['moving_time'], "date": a['start_date']} for a in activities_data]
    prompt = f"Voici mes 5 dernières activités de running : {summary}. Sans rentrer dans les détails, que peux-tu me dire sur ma progression et mes performances ? Donne moi un feedback global et des conseils pour m'améliorer. Fais cela en moins de 100 mots."
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )
    return response.text