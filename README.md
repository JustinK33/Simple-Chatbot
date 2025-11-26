# Burnt-Out CS Tutor 😵‍💻

A simple terminal-based chatbot powered by **Google Gemini** (via `llama_index`) that roleplays as a **burnt-out computer science tutor**.

---

## Features

- Uses **Google Gemini** via `llama_index.llms.google_genai.GoogleGenAI`
- Persistent conversation context with `ChatMessage`
- Personality:
  - Calls you *nerd* sometimes
  - A bit sarcastic, but still explains things step-by-step
  - Tries to be supportive if you seem stressed

---

## Requirements

- Python **3.11+**
- A **Google AI Studio / Gemini API key**
- (Optional) Docker, if you want to run it in a container

---

## Setup (Local Python)

git clone <your-repo-url>.git
cd ChatBot   # or whatever your project folder is called

python3 -m venv venv
source venv/bin/activate   # on macOS / Linux

pip install -r requirements.txt

GOOGLE_API_KEY=your_real_api_key_here # set this in your .env file

python3 app/main.py # run it locally

docker build -t cstutor -f dockerfile . 
docker run --rm -it --env-file .env cstutor # run it with docker
