# BUILD A CHATBOT USING NATURAL LANGUAGE PROCESSING LIBRARIES LIKE NLTK OR SPACY, CAPABLE OF ANSWERING USER QUERIES. DELIVERABLE: A PYTHON SCRIPT AND A WORKING CHATBOT.
# chatbot_nlp.py

import random
import re
import nltk
import spacy

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK resources (first time only)
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab") # Added this line to download the missing resource

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined intents/responses
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey! Need any assistance?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "name": ["I am your friendly chatbot.", "People call me ChatBot!", "I'm just a simple NLP chatbot."],
    "default": ["I'm not sure about that. Could you rephrase?", "Sorry, I don’t understand.", "Let's talk about something else!"]
}

# Intent detection function
def get_intent(user_input):
    user_input = user_input.lower()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "greeting"
    elif re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return "goodbye"
    elif re.search(r"\b(thank|thanks)\b", user_input):
        return "thanks"
    elif re.search(r"\b(name|who are you)\b", user_input):
        return "name"
    else:
        return "default"

# Preprocessing with NLTK
def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [w for w in tokens if w.isalpha() and w not in stop_words]
    return filtered_tokens

# Chat function
def chatbot():
    print("ChatBot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ChatBot: Bye! Have a nice day.")
            break

        tokens = preprocess(user_input)
        intent = get_intent(" ".join(tokens))
        response = random.choice(responses[intent])
        print("ChatBot:", response)

if __name__ == "__main__":
    chatbot()