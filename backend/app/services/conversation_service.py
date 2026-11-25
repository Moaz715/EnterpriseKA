
from sqlalchemy.orm import Session

from app.models.conversation import Conversation


def create_conversation(db: Session, user_id: int, title: str):
    new_conversation = Conversation(user_id=user_id, title=title)

    db.add(new_conversation)
    db.commit()
    db.refresh(new_conversation)

    return new_conversation


def get_conversations(db: Session, user_id: int, skip: int, limit: int):
    conversations = db.query(Conversation).filter(Conversation.user_id == user_id).offset(skip).limit(limit).all()
    return conversations

def get_conversation(db: Session, user_id: int, conversation_id: int):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id, Conversation.user_id == user_id).first()
    if conversation is None:
        return None
    return conversation

def update_conversation(db: Session, user_id: int, conversation_id: int, title: str):
    conversation = db.query(Conversation).filter(conversation.id == conversation_id, Conversation.user_id == user_id).first()
    if conversation is None:
        return None
    
    conversation.title = title
    db.commit()
    db.refresh(conversation)
    
    return conversation

def delete_conversation(db: Session, user_id: int, conversation_id: int):
    conversation = db.query(Conversation).filter(conversation.id == conversation_id, Conversation.user_id == user_id).first()
    if conversation is None:
        return False
    
    db.delete(conversation)
    db.commit()
    
    return True
    