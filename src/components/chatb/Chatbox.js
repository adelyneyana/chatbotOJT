import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';

const Chatbox = () => {
  const [conversation, setConversation] = useState([]);
  const [message, setMessage] = useState('');
  const conversationEndRef = useRef(null); // Ref to scroll to the bottom of the conversation

  // Scroll to the bottom of the conversation whenever it updates
  useEffect(() => {
    conversationEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [conversation]);

  const sendMessage = async (userMessage) => {
    // Display the user's message in the chatbox
    setConversation((prevConversation) => [
      ...prevConversation,
      { user: true, text: userMessage },
    ]);

    // Call the backend API for response and suggested replies
    try {
      const response = await axios.post('http://localhost:5000/chat', { message: userMessage });

      // Add the agent's response and suggestions
      setConversation((prevConversation) => [
        ...prevConversation,
        { user: false, text: response.data.agent_reply, suggestions: response.data.suggestions },
      ]);
    } catch (error) {
      console.error("Error sending message:", error);
    }

    setMessage('');
  };

  const handleSuggestionClick = (suggestion) => {
    // If the user clicks a suggestion, send that suggestion as a new message
    sendMessage(suggestion);
  };

  return (
    <div className="chatbox">
      <div className="conversation">
        {conversation.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.user ? 'user-message' : 'agent-message'}`}
          >
            <div className={`message-bubble ${msg.user ? 'user-bubble' : 'agent-bubble'}`}>
              <p>{msg.text}</p>
            </div>
            {msg.suggestions && (
              <div className="suggestions">
                {msg.suggestions.map((suggestion, idx) => (
                  <button
                    key={idx}
                    className="suggestion-button"
                    onClick={() => handleSuggestionClick(suggestion)}
                  >
                    {suggestion}
                  </button>
                ))}
              </div>
            )}
          </div>
        ))}
        <div ref={conversationEndRef} />
      </div>

      <div className="input-container">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={() => sendMessage(message)}>Send</button>
      </div>
    </div>
  );
};

export default Chatbox;
