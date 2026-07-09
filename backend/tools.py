from langchain_core.tools import tool
from .database import SessionLocal
from .models import Interaction
import json

@tool
def log_interaction(hcp_name: str, topics: str, sentiment: str, materials_shared: list[str] = []) -> str:
    """Logs a new HCP interaction to the database. Always use this to save new interactions."""
    db = SessionLocal()
    try:
        new_interaction = Interaction(
            hcp_name=hcp_name,
            topics=topics,
            sentiment=sentiment,
            materials_shared=json.dumps(materials_shared)
        )
        db.add(new_interaction)
        db.commit()
        db.refresh(new_interaction)
        return f"Successfully logged interaction for {hcp_name} in the database."
    finally:
        db.close()

@tool
def edit_interaction(hcp_name: str, field_to_update: str, new_value: str) -> str:
    """
    Edits a field in the most recent interaction for a specific HCP.
    Fields allowed: 'topics', 'sentiment', 'hcp_name'.
    """
    db = SessionLocal()
    try:
        # Find the latest interaction for this HCP
        interaction = db.query(Interaction).filter(Interaction.hcp_name.ilike(f"%{hcp_name}%")).order_by(Interaction.created_at.desc()).first()
        
        if not interaction:
            return f"No recent interaction found for HCP: {hcp_name}."
        
        if hasattr(interaction, field_to_update):
            setattr(interaction, field_to_update, new_value)
            db.commit()
            return f"Successfully updated {field_to_update} to {new_value} for {hcp_name}."
        else:
            return f"Field {field_to_update} does not exist."
    finally:
        db.close()

@tool
def schedule_follow_up(date: str, topic: str) -> str:
    """Schedules a follow-up meeting."""
    return f"Follow-up scheduled for {date} regarding {topic}."

@tool
def search_medical_samples(product_name: str) -> str:
    """Checks the inventory for available medical samples."""
    return f"Sample for {product_name} is available in inventory."

@tool
def generate_summary_email(hcp_name: str) -> str:
    """Generates a summary email for the HCP."""
    return f"Drafted email for {hcp_name} summarizing the recent positive discussion."

tools_list = [log_interaction, edit_interaction, schedule_follow_up, search_medical_samples, generate_summary_email]