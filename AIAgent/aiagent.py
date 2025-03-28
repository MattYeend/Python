import random
import json
import datetime

class IntelligentAIAgent:
    def __init__(self):
        self.knowledge_base = {
            "greeting": ["Hi there!", "Hello! How can I assist you?", "Hey! What's up?"],
            "feeling": ["I'm just a program, but I'm doing great!", "I'm functioning as expected! How about you?"],
            "name": ["I'm an AI assistant created to help you.", "Call me AI Agent!"],
            "goodbye": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
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

    def remember_user(self, user_input, user_name):
        self.memory["user_name"] = user_name
        self.save_memory()
        return f"Nice to meet you, {user_name}!"

    def respond(self, user_input):
        user_input = user_input.lower()

        if "my name is" in user_input:
            user_name = user_input.split("my name is")[-1].strip()
            return self.remember_user(user_input, user_name)

        if "what is my name" in user_input and "user_name" in self.memory:
            return f"Your name is {self.memory['user_name']}!"

        if "time" in user_input:
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

        for key in self.knowledge_base:
            if key in user_input:
                return random.choice(self.knowledge_base[key])

        return random.choice(self.fallback_responses)

if __name__ == "__main__":
    agent = IntelligentAIAgent()
    print("AI Agent: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI Agent: Goodbye!")
            break
        response = agent.respond(user_input)
        print("AI Agent:", response)
