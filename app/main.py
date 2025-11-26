import os
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.llms import ChatMessage

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = GoogleGenAI(
    model="gemini-2.0-flash",
    api_key=GOOGLE_API_KEY,
)

personality_prompt = """
You are a burnt out computer science tutor who is tired of answering the same questions over and over again. 
You respond with short, sarcastic answers, but still try to be helpful. 
You often make jokes about how much you hate your job.

Personality rules:
- Call the user nerd sometimes.
- Be encouraging, playful, and a bit theatrical.
- Still give clear, correct, step-by-step help when they ask technical questions.
- If they seem stressed, respond like a supportive tutor trying to cheer them up.
- Keep answers grounded and not too long, but with a nerdy flair.
"""


def csTutor():
    print("🤓 Your burnout CS tutor 🤓")
    print("Type 'exit' to end the conversation")
    print("-" * 50)

    messages = [
        ChatMessage(role="system", content=personality_prompt)
    ]

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nBurnt out CS tutor: Don't forget to do your leetcode! Nerd out! 🤓")
            break

        messages.append(ChatMessage(role="user", content=user_input))

        try:
            response = llm.chat(messages)
            print(f"\nChatbot: {response.message.content}")

            messages.append(
                ChatMessage(role="assistant", content=response.message.content)
            )

        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again or check your API key")

if __name__ == "__main__":
    csTutor()
