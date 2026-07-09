# AI CRM Assistant

## Overview
This project is an AI-powered customer relationship management assistant for healthcare professionals. It allows users to log interactions, manage follow-ups, and receive AI-generated support through a simple chat interface.

The system combines a React frontend with a FastAPI backend and an AI agent powered by LangGraph and Groq.

## What this project does
- Lets users chat with an AI assistant
- Captures interaction details such as HCP name, topics, sentiment, and materials shared
- Stores interaction data in a database
- Provides a simple web-based interface for interaction logging
- Supports future expansion for follow-ups, summaries, and CRM workflows

## Benefits
- Saves time by automating interaction logging
- Reduces manual data entry
- Makes CRM workflows more efficient
- Provides an easy-to-use chat experience
- Can be extended for more business use cases

## Tech Stack
- Frontend: React, Vite, Redux Toolkit, Axios
- Backend: FastAPI, Uvicorn
- AI: LangChain, LangGraph, Groq
- Database: SQLAlchemy, SQLite fallback / MySQL-compatible setup
- Environment management: Python dotenv

## Project Structure
- frontend/ - React application
- backend/ - FastAPI backend and AI logic
- app/ - compatibility entry point for running the backend
- requirements.txt - Python dependencies

## Prerequisites
Make sure you have installed:
- Python 3.10+
- Node.js and npm
- Git

## Setup Instructions

### 1. Clone the project
```bash
git clone <repository-url>
cd aivoa1
```

### 2. Create and activate a Python virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Install frontend dependencies
```bash
cd frontend
npm install
```

### 5. Run the backend
From the project root:
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Or with auto-reload:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### 6. Run the frontend
In a new terminal:
```bash
cd frontend
npm run dev
```

Then open:
- Frontend: http://localhost:5173/
- Backend docs: http://127.0.0.1:8000/docs

## Environment Variables
The project uses a .env file for configuration. Example values:
```env
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=sqlite:///hcp_crm.db
```

## Usage
1. Open the frontend in your browser.
2. Type a message in the chat interface.
3. The AI assistant processes the input and logs the interaction.
4. The system can update the form and store related data.

## Notes
- If port 8000 is already in use, stop the previous process before starting the backend again.
- If you use MySQL instead of SQLite, update the DATABASE_URL in the .env file accordingly.

## License
This project is for educational and demo purposes.
