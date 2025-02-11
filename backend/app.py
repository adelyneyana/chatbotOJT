from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- Import this
from transformers import pipeline

app = Flask(__name__)

# Enable CORS
CORS(app)  # This will allow all origins by default

qa_pipeline = pipeline("question-answering")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  # Expecting a JSON payload with 'message'
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400
    
    # Here, you can adjust the logic to handle the user message
    # For this example, we're using the same question-answering pipeline as before
    context = "France is a country in Europe. The capital of France is Paris."
    question = user_message
    
    result = qa_pipeline({
        'context': context,
        'question': question
    })
    
    agent_reply = result['answer']  # Getting the answer from the model
    suggestions = ["Did you mean something else?", "Can you clarify?"]  # Example suggestions
    
    return jsonify({
        "agent_reply": agent_reply,
        "suggestions": suggestions
    })

if __name__ == "__main__":
    app.run(debug=True)
