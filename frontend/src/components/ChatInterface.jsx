import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addMessage, updateFormData, setLoading } from '../store/interactionSlice';
import { Send, Bot, User } from 'lucide-react';
import axios from 'axios';

export default function ChatInterface() {
  const [input, setInput] = useState('');
  const dispatch = useDispatch();
  const { messages, isLoading } = useSelector((state) => state.interaction);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg = input.trim();
    setInput('');
    dispatch(addMessage({ role: 'user', content: userMsg }));
    dispatch(setLoading(true));

    try {
      // Call FastAPI Backend
      const response = await axios.post('http://127.0.0.1:8000/chat', {
        message: userMsg,
        thread_id: 'react-user-session-1'
      });

      // Update Chat
      dispatch(addMessage({ role: 'ai', content: response.data.response }));
      
      // Auto-fill the form with database record
      if (response.data.latest_db_record) {
        dispatch(updateFormData(response.data.latest_db_record));
      }
    } catch (error) {
      dispatch(addMessage({ role: 'ai', content: 'Error: Could not connect to AI Agent.' }));
    } finally {
      dispatch(setLoading(false));
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <Bot size={20} className="icon-blue" />
        <h3>AI Assistant</h3>
      </div>
      
      <div className="messages-area">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message-bubble ${msg.role}`}>
            {msg.role === 'ai' ? <Bot size={16} /> : <User size={16} />}
            <p>{msg.content}</p>
          </div>
        ))}
        {isLoading && <div className="loading">AI is thinking and updating form...</div>}
      </div>

      <div className="chat-input-area">
        <input 
          type="text" 
          value={input} 
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Describe interaction..." 
        />
        <button onClick={handleSend} disabled={isLoading}>
          <Send size={18} /> Log
        </button>
      </div>
    </div>
  );
}