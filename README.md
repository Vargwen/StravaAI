# Strava AI Coach
Strava AI Coach is a Streamlit application that synchronizes your Strava sports activities and generates personalized analyses using Google's AI (Gemini).

## 🚀 Features
**Strava Authentication:** Secure connection via OAuth2.

**Persistent Management:** Uses a SQLite database to securely store access tokens (refresh tokens).

**AI Analysis: Intelligent** feedback on your athletic performance provided by Gemini.

**Intuitive Interface:** Clean and modern dashboard built with Streamlit.

## 🛠 Local Installation
Clone the repository:
'''bash
git clone https://github.com/your-username/strava-ai-coach.git

Install the dependencies:
'''bash
pip install -r requirements.txt

Create a .env file with your keys:
'''bash
STRAVA_CLIENT_ID=your_id
STRAVA_CLIENT_SECRET=your_secret
GEMINI_API_KEY=your_gemini_key

Run the application:
'''bash
streamlit run app.py

## ☁️ Cloud Deployment (Streamlit Community Cloud)
Push your code to GitHub (ensure .env and .db files are ignored).

Connect your repository to share.streamlit.io.

Add your keys in the "Secrets" section of your app settings:

'''bash
STRAVA_CLIENT_ID = "your_id"
STRAVA_CLIENT_SEStrava AI Coach
Strava AI Coach is a Streamlit application that synchronizes your Strava sports activities and generates personalized analyses using Google's AI (Gemini).

🚀 Features
Strava Authentication: Secure connection via OAuth2.

Persistent Management: Uses a SQLite database to securely store access tokens (refresh tokens).

AI Analysis: Intelligent feedback on your athletic performance provided by Gemini.

Intuitive Interface: Clean and modern dashboard built with Streamlit.

🛠 Local Installation
Clone the repository:

Bash
git clone https://github.com/your-username/strava-ai-coach.git
Install the dependencies:

Bash
pip install -r requirements.txt
Create a .env file with your keys:

Plaintext
STRAVA_CLIENT_ID=your_id
STRAVA_CLIENT_SECRET=your_secret
GEMINI_API_KEY=your_gemini_key
Run the application:

Bash
streamlit run app.py
☁️ Cloud Deployment (Streamlit Community Cloud)
Push your code to GitHub (ensure .env and .db files are ignored).

Connect your repository to share.streamlit.io.

Add your keys in the "Secrets" section of your app settings:

Ini, TOML
STRAVA_CLIENT_ID = "your_id"
STRAVA_CLIENT_SECRET = "your_secret"
GEMINI_API_KEY = "your_gemini_key"
🏗 Project Structure
app.py: User interface and core application logic.

sqlite.py: Database management for users.db.

getUserToken.py: OAuth token refresh logic.

gemAnalysis.py: Integration with the Gemini API.CRET = "your_secret"
GEMINI_API_KEY = "your_gemini_key"

## 🏗 Project Structure
app.py: User interface and core application logic.

sqlite.py: Database management for users.db.

getUserToken.py: OAuth token refresh logic.

gemAnalysis.py: Integration with the Gemini API.
