<<<<<<< HEAD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_data = [
    ("What is AI?", "AI means Artificial Intelligence."),
    ("What is Python?", "Python is a programming language."),
    ("What is NLP?", "NLP helps computers understand language.")
]

questions = [q for q, a in faq_data]
answers = [a for q, a in faq_data]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

def chatbot(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, faq_vectors)

    index = similarity.argmax()
    return answers[index]

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
=======
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_data = [
    ("What is AI?", "AI means Artificial Intelligence."),
    ("What is Python?", "Python is a programming language."),
    ("What is NLP?", "NLP helps computers understand language.")
]

questions = [q for q, a in faq_data]
answers = [a for q, a in faq_data]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

def chatbot(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, faq_vectors)

    index = similarity.argmax()
    return answers[index]

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break
>>>>>>> 3528fe8f6f47fc1680d4962056169065290ebf42
    print("Bot:", chatbot(user))