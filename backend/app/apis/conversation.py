from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.conversation import ConversationCreate, ConversationRead, ConversationUpdate
from app.services import conversation_service

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


@router.post("/", response_model=ConversationRead)
def create_conversation(conversation: ConversationCreate, db: Session = Depends(get_db)):
    return conversation_service.create_conversation(db=db, user_id=1,title=conversation.title)

@router.get("/", response_model=List[ConversationRead])
def get_conversations(db: Session = Depends(get_db), skip: int = 0, limit: int = 20):
    return conversation_service.get_conversations(db=db, user_id = 1, skip=skip, limit=limit)

@router.get("/{conversation_id}", response_model=ConversationRead)
def get_conversation(conversation_id: int, db: Session = Depends(get_db)):
    conversation = conversation_service.get_conversation(db=db, user_id=1, conversation_id=conversation_id)
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation

@router.patch("/{conversation_id}", response_model=ConversationRead)
def update_conversation(data: ConversationUpdate, conversation_id: int, db: Session = Depends(get_db)):
    conversation = conversation_service.update_conversation(db=db, user_id=1, conversation_id=conversation_id, title=data.title)

    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return conversation

@router.delete("/{conversation_id}")
def delete_conversation(conversation_id: int, db: Session = Depends(get_db)):
    check = conversation_service.delete_conversation(db=db, user_id=1, conversation_id=conversation_id)

    if not check:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return {"message": "Conversation deleted successfully"}