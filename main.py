from getUserToken import get_token
from getUserActivities import get_activities
from gemAnalysis import analyze_with_gemini

def main():
    # A. Récupérer un token valide
    token = get_token()

    # B. Récupérer les données
    activities = get_activities(token)

    # C. Analyser
    feedback = analyze_with_gemini(activities)
    print("\n--- Feedback de Gemini ---")
    print(feedback)

# --- Exécution principale ---
if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"Une erreur est survenue : {e}")