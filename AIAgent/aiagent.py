import random
import json
import datetime
import re
from fuzzywuzzy import process

class SmartAIAgent:
    def __init__(self):
        self.knowledge_base = {
            "hello": ["Hi there!", "Hello! How can I assist you?", "Hey! What's up?"],
            "how are you": ["I'm just a program, but I'm doing great!", "I'm functioning as expected! How about you?"],
            "your name": ["I'm an AI assistant created to help you.", "Call me AI Agent!"],
            "bye": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
            "time": [lambda: f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"],
            "date": [lambda: f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"],
            "weather": ["I can't fetch live weather updates, but you can check a weather website!"]
        }
        self.fallback_responses = [
            "I'm not sure how to respond to that.",
            "Can you rephrase that?",
            "I'm still learning. Could you clarify?"
        ]
        self.memory = {}
        self.load_memory()

    def save_memory(self):
        with open("memory.json", "w") as file:
            json.dump(self.memory, file)

    def load_memory(self):
        try:
            with open("memory.json", "r") as file:
                self.memory = json.load(file)
        except FileNotFoundError:
            self.memory = {}

    def remember_user(self, user_input):
        match = re.search(r"my name is (.+)", user_input, re.IGNORECASE)
        if match:
            user_name = match.group(1).strip()
            self.memory["user_name"] = user_name
            self.save_memory()
            return f"Nice to meet you, {user_name}!"
        return "I didn't catch your name. Could you repeat it?"

    def respond(self, user_input):
        user_input = user_input.lower()

        # Check for direct greetings
        greetings = ["hi", "hello", "hey", "howdy", "yo"]
        if any(greeting in user_input for greeting in greetings):
            return random.choice(self.knowledge_base["hello"])

        # Respond to "how are you"
        if "how are you" in user_input:
            return random.choice(self.knowledge_base["how are you"])

        # Respond to "what is your name" or similar
        if "what is your name" in user_input or "your name" in user_input:
            return random.choice(self.knowledge_base["your name"])

        if "my name is" in user_input:
            return self.remember_user(user_input)

        if "what is my name" in user_input and "user_name" in self.memory:
            return f"Your name is {self.memory['user_name']}!"

        # Fuzzy matching if no direct match found
        best_match, score = process.extractOne(user_input, self.knowledge_base.keys())
        
        if score > 50:  # We lowered the threshold to 50 to catch more variations
            response = random.choice(self.knowledge_base[best_match])
            return response() if callable(response) else response

        return random.choice(self.fallback_responses)

if __name__ == "__main__":
    agent = SmartAIAgent()
    print("AI Agent: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI Agent: Goodbye!")
            break
        response = agent.respond(user_input)
        print("AI Agent:", response)