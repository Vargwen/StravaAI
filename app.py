import streamlit as st
import json
import os
from dotenv import load_dotenv
from getUserToken import get_token, get_user_token
from getUserActivities import get_activities
from gemAnalysis import analyze_with_gemini

st.title("Strava AI Coach")

# On vérifie si strava a renvoyé le code dans l'URL
query_params = st.query_params
code = query_params.get("code")

# Nouveau venu ou première connexion : on récupère le token et on le stocke dans la session
if code and 'athlete_id' not in st.session_state:
    athelete_id, token = get_token(code)
    st.session_state['athlete_id'] = athelete_id
    st.query_params.clear()
    st.rerun()

# Utilisateur connu, on rafraichit son accès
elif 'athlete_id' in st.session_state:
    token = get_user_token(st.session_state['athlete_id'])

    activities = get_activities(token)

    st.write("Voici vos dernières courses :")
    for act in activities:
        st.write(f"- {act['name']} : {act['distance']/1000:.2f} km en {act['moving_time']//60} min le {act['start_date'][:10]}")

    feedback = analyze_with_gemini(activities)
    st.subheader("Feedback de Gemini")
    st.write(feedback)

else:
    st.info("Veuillez vous connecter pour voir vos activités")

    # URL
    client_id = os.getenv("STRAVA_CLIENT_ID")
    redirect_uri = "http://localhost:8501"
    auth_url = f"https://www.strava.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=activity:read_all"

    st.link_button("Se connecter avec strava", url=auth_url)