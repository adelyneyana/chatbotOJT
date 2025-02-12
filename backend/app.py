from flask import Flask, request, jsonify, session
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session handling

# Enable CORS
CORS(app)

qa_pipeline = pipeline("question-answering")

# Example static contexts for different topics
contexts = {
    "france": "France is a country in Europe. The capital of France is Paris. It is known for its art, fashion, and culture.",
    "language_in_france": "The official language spoken in France is French.",
    "weather_in_france": "The climate in France varies depending on the region. Northern France has a temperate climate, while southern France has a Mediterranean climate.",
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  # Expecting a JSON payload with 'message'
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400
    
    # Initialize conversation history in session if it's not already there
    if "conversation_history" not in session:
        session["conversation_history"] = []
    
    # Add user message to conversation history
    session["conversation_history"].append(f"User: {user_message}")
    
    # Determine the context dynamically based on the user's message
    context = None
    if "france" in user_message.lower():
        context = contexts["france"]
        if "language" in user_message.lower():
            context = contexts["language_in_france"]
        elif "weather" in user_message.lower():
            context = contexts["weather_in_france"]
    
    if context is None:
        context = "I can talk about various topics like countries, technology, and history."

    # Use the context along with the user's message to generate a response
    result = qa_pipeline({
        'context': context,
        'question': user_message
    })
    
    agent_reply = result['answer']  # Getting the answer from the model
    
    # Decide whether to show suggestions based on the content of the answer
    if "varies depending on the region" in agent_reply or "country in Europe" in agent_reply:
        suggestions = [
            "Did you mean something else?", 
            "Can you clarify your question?",
            "Would you like more information on this topic?"
        ]
    else:
        suggestions = []
    
    # Add the agent's reply to the conversation history
    session["conversation_history"].append(f"Agent: {agent_reply}")
    
    return jsonify({
        "agent_reply": agent_reply,
        "suggestions": suggestions
    })

if __name__ == "__main__":
    app.run(debug=True)
