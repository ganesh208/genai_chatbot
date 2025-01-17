import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
  const [userQuery, setUserQuery] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userQuery.trim()) return; // Don't send empty queries

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/query', {
        user_query: userQuery,
      });

      // Add the user query and bot response to the chat history
      setChatHistory((prevHistory) => [
        ...prevHistory,
        { user: userQuery, bot: response.data.response },
      ]);
      setUserQuery(''); // Clear input field
    } catch (error) {
      console.error('Error while sending query:', error);
      alert('Something went wrong. Please try again!');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <h2>Chatbot</h2>
      <div className="chat-box">
        {chatHistory.map((message, index) => (
          <div key={index} className="message">
            <div className="user-query">
              <strong>You:</strong> {message.user}
            </div>
            <div className="bot-response">
              <strong>Bot:</strong> {message.bot}
            </div>
          </div>
        ))}
        {loading && <div>Loading...</div>}
      </div>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={userQuery}
          onChange={(e) => setUserQuery(e.target.value)}
          placeholder="Ask me something..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default Chatbot;
