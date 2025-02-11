import React, { useState } from 'react';
import axios from 'axios';

const Chatbox = () => {
  const [conversation, setConversation] = useState([]);
  const [message, setMessage] = useState('');

  const sendMessage = async () => {
    // Display the user's message in the chatbox
    setConversation([...conversation, { user: true, text: message }]);
    
    // Call the backend API for response and suggested replies
    const response = await axios.post('http://localhost:5000/chat', { message });
    
    // Add the agent's response and suggestions
    setConversation([
      ...conversation, 
      { user: false, text: response.data.agent_reply, suggestions: response.data.suggestions }
    ]);
    
    setMessage('');
  };

  return (
    <div className="chatbox">
      <div className="conversation">
        {conversation.map((msg, index) => (
          <div key={index} className={msg.user ? 'user-message' : 'agent-message'}>
            <p>{msg.text}</p>
            {msg.suggestions && (
              <div className="suggestions">
                {msg.suggestions.map((suggestion, idx) => (
                  <button key={idx} onClick={() => sendMessage(suggestion)}>{suggestion}</button>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>

      <div className="input-container">
        <input 
          type="text" 
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..." 
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbox;
