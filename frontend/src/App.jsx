import React from 'react';
import InteractionForm from './components/InteractionForm';
import ChatInterface from './components/ChatInterface';
import './App.css';

function App() {
  return (
    <div className="app-layout">
      <InteractionForm />
      <ChatInterface />
    </div>
  );
}

export default App;