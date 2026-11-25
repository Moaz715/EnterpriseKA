from sqlalchemy.orm import Session

from app.models.message import Message
from app.models.enums import MessageRole

def create_message(db: Session, conversation_id: int, content: str, role: MessageRole):
    new_message = Message(conversation_id=conversation_id, content=content, role=role)
    
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    
    return new_message

def get_messages(db: Session, conversation_id: int):
    messages = db.query(Message).filter(Message.conversation_id == conversation_id).order_by(Message.created_at.asc()).all()
    return messages

