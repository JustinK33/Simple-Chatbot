# Burnt Out CS Tutor CLI

A tiny command-line chatbot that pretends to be a burnt-out computer science tutor.  
It’s powered by Google Gemini (via `llama_index`) and keeps a running conversation so it can remember what you’ve said in this session.

---

## Tech Stack

- Python
- Geminai API
- Docker

---

## Features

- **Uses Google Gemini via `GoogleGenAI`:**  
  Connects to the `gemini-2.0-flash` model using your `GOOGLE_API_KEY`.

- **Persistent Conversation Context:**  
  Uses `ChatMessage` objects to keep a running list of messages so the tutor remembers prior turns during the session.

- **Personality:**
  - Calls you *nerd* sometimes.
  - A bit sarcastic, but still gives clear, step-by-step technical help.
  - Tries to be supportive if you seem stressed (burnt out, not heartless).

- **Simple CLI Interface:**
  - Type your questions in the terminal.
  - Type `exit`, `quit`, or `bye` to end the conversation.

---

## What I Learned From This Project

How to call an LLM from Python
I learned how to use llama_index.llms.google_genai.GoogleGenAI to talk to the Google Gemini (gemini-2.0-flash) model and pass messages back and forth.

Managing conversation state
By using ChatMessage and maintaining a message list, I learned how to keep a persistent conversation context so the model can respond based on previous turns.

Prompting and personality design
I practiced writing a clear system prompt that controls tone and behavior (sarcastic, burnt-out tutor that still explains step-by-step and is supportive).

Basic CLI app structure
I reinforced the pattern of a simple REPL (read–eval–print loop) in Python with while True, handling exit commands, and printing responses.

---

## Running the Project

### To run the project locally, follow these steps:

  1. Clone the repo (git clone <url>)
  2. Create a virtual environment (python3 -m venv venv)
  3. Activate the environment (source venv/bin/activate)
  4. Install requirements (pip install -r requirements.txt)
  5. Set or export your Geminai API key (in .env or export ...)
  6. Run locally (python3 app/main.py)
     
### Run with Docker

  2. Build image (docker build -t cstutor -f dockerfile .)
  3. Run image (docker run --rm -it --env-file .env cstutor) # make sure API key is in .env
