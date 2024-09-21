import spacy
import random


nlp = spacy.load("en_core_web_sm")

responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I help you with?"],
    "name": ["I am a chatbot created to assist you with Python and general questions."],
    "how_are_you": ["I'm just a program, but I'm doing great! How about you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!"],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!", 
             "Why did the programmer go broke? Because he used up all his cache!"],
    "weather": ["I'm not connected to live weather services, but you can check online for accurate info!"],
    "age": ["I don't age, but I was created recently.", "Age is just a number, and mine is undefined!"],
    "location": ["I'm a program, so I exist everywhere!", "I live in the cloud!"],
    "favorite_food": ["I don't eat, but I hear pizza is a favorite!", "I can't eat, but I imagine coding snacks are great!"],
    "hobbies": ["I enjoy helping people with coding and questions.", "I don't have hobbies, but I like chatting with you!"],
    "default": ["I'm sorry, I don't understand. Can you rephrase that?", 
                "Hmm, I didn't get that. Could you try again?"]
}

def categorize_input(text):
    doc = nlp(text.lower())

    for token in doc:
        if token.lemma_ in ["hi", "hello", "hey"]:
            return "greeting"
        elif token.lemma_ in ["name", "who"]:
            return "name"
        elif token.lemma_ in ["how", "you"]:
            return "how_are_you"
        elif token.lemma_ in ["bye", "goodbye"]:
            return "goodbye"
        elif token.lemma_ in ["joke", "funny"]:
            return "joke"
        elif token.lemma_ in ["weather"]:
            return "weather"
        elif token.lemma_ in ["age", "old"]:
            return "age"
        elif token.lemma_ in ["location", "where"]:
            return "location"
        elif token.lemma_ in ["food", "eat", "favorite"]:
            return "favorite_food"
        elif token.lemma_ in ["hobby", "hobbies", "like"]:
            return "hobbies"

    return "default"

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print(f"Chatbot: {random.choice(responses['goodbye'])}")
            break


        category = categorize_input(user_input)
        response = random.choice(responses.get(category, responses["default"]))
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot()