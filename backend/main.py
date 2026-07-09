from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .models import Interaction
from .agent import process_chat

app = FastAPI(title="AI-First CRM HCP Module")

# --- BULLETPROOF CORS SETTING ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # Ab yeh har website ko allow karega
    allow_credentials=False,     # Isko False karna sabse zaroori tha
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------------

# 3. Database tables create karein
try:
    Base.metadata.create_all(bind=engine)
except Exception:
    pass

# 4. Endpoints define karein
class ChatRequest(BaseModel):
    message: str
    thread_id: str = "default-thread"

class ChatResponse(BaseModel):
    response: str
    latest_db_record: Optional[dict] = None

@app.post("/chat", response_model=ChatResponse)
def chat_with_agent(request: ChatRequest, db: Session = Depends(get_db)):
    ai_response = process_chat(request.message, request.thread_id)
    latest_interaction = db.query(Interaction).order_by(Interaction.created_at.desc()).first()
    
    db_record = None
    if latest_interaction:
        db_record = {
            "hcp_name": latest_interaction.hcp_name,
            "interaction_type": latest_interaction.interaction_type,
            "topics": latest_interaction.topics,
            "sentiment": latest_interaction.sentiment,
            "materials_shared": latest_interaction.materials_shared
        }
    
    return ChatResponse(
        response=ai_response,
        latest_db_record=db_record
    )