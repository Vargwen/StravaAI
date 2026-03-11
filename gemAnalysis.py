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
    prompt = f"Analyse ces dernières activités sportives : {summary}. Résume en quelques phrases les activités de running pour me donner un aperçu de mon évolution en étant concis. Sois objectifs et montre s'il y a des points d'amélioration. Prend en compte la date pour respecter la chronologie. Ne donne pas le détail des activités"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )
    return response.text