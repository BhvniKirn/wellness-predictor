import json
import random
import pickle
import numpy as np

import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')


# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

stemmer = PorterStemmer()

# Preprocessing
all_patterns = []
all_tags = []
tag_to_response = {}

for intent in data["intents"]:
    tag = intent["tag"]
    tag_to_response[tag] = intent["responses"]
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)

        stemmed = [stemmer.stem(w.lower()) for w in tokens]
        all_patterns.append(" ".join(stemmed))
        all_tags.append(tag)

# Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(all_patterns)
y = np.array(all_tags)

# Model training
model = LogisticRegression()
model.fit(X, y)

# Save model and tools
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("tag_responses.pkl", "wb") as f:
    pickle.dump(tag_to_response, f)

print("Chatbot model trained and saved.")


