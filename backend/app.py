from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # To allow frontend requests

# Load NLP models
nlp = spacy.load("en_core_web_sm")
qa_pipeline = pipeline("question-answering")

# Simple in-memory conversation log
conversation_log = []

# Function to generate agent response and suggestions
def generate_reply(client_message):
    # Example NLP task (spaCy)
    doc = nlp(client_message)
    entities = [ent.text for ent in doc.ents]

    # Use Hugging Face for more advanced responses
    context = "This is a general FAQ or knowledge base."
    answer = qa_pipeline(question=client_message, context=context)

    # Return a simple agent response and some suggestions
    return f"Agent response: {answer['answer']}", ["Reply 1", "Reply 2", "Reply 3"]

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    client_message = data.get("message")

    # Generate response and suggestions
    agent_reply, suggestions = generate_reply(client_message)

    # Log the conversation
    conversation_log.append({"client": client_message, "agent": agent_reply})

    return jsonify({
        "agent_reply": agent_reply,
        "suggestions": suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)
