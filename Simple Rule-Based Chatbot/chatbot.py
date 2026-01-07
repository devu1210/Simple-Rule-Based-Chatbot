import re
import json
from datetime import datetime

# Load Knowledge Base
with open("knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

# Intent Patterns
INTENT_PATTERNS = {
    "greeting": re.compile(r"\b(hi|hello|hey|good morning|good evening)\b"),
    "help": re.compile(r"\b(help|support|assist)\b"),
    "thanks": re.compile(r"\b(thanks|thank you)\b"),
    "bye": re.compile(r"\b(bye|exit|quit)\b"),
}

INTENT_RESPONSES = {
    "greeting": "Hello! I am an AI chatbot. How can I help you?",
    "help": "You can ask me general questions about AI, ML, or this internship.",
    "thanks": "You're welcome! 😊",
    "bye": "Goodbye! Have a great day!"
}

# Logging
def log_conversation(user, bot):
    with open("chat_log.txt", "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] User: {user}\n")
        f.write(f"[{time}] Bot : {bot}\n")

# Knowledge Base Lookup 
def knowledge_lookup(user_input):
    user_input = user_input.lower()
    for question, answer in knowledge_base.items():
        if question in user_input:
            return answer
    return None

# Intent Detection
def detect_intent(user_input):
    for intent, pattern in INTENT_PATTERNS.items():
        if pattern.search(user_input):
            return intent
    return None

# Main ChatLoop
def chat():
    print("🤖 AI Chatbot Started (type 'exit' to quit)")
    print("------------------------------------------")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        intent = detect_intent(user_input)

        if intent:
            response = INTENT_RESPONSES[intent]
            print("Bot:", response)
            log_conversation(user_input, response)

            if intent == "bye":
                break
            continue

        kb_response = knowledge_lookup(user_input)
        if kb_response:
            print("Bot:", kb_response)
            log_conversation(user_input, kb_response)
        else:
            fallback = "Sorry, I don't understand that yet. Try asking something else."
            print("Bot:", fallback)
            log_conversation(user_input, fallback)

# Run
if __name__ == "__main__":
    chat()
