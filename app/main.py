import os
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.llms import ChatMessage

llm = GoogleGenAI(
    model="gemini-2.0-flash",
)

def simple_chatbot():
    print("🦙 Simple Gemini Chatbot 🦙")
    print("Type 'exit' to end the conversation")
    print("-" * 50)

    messages = []

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\nChatbot: Goodbye! Have a great day!")
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
    simple_chatbot()
