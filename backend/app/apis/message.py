from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.message import MessageCreate, MessageRead
from app.services import message_service
from app.models.enums import MessageRole

router = APIRouter(
    prefix="/conversations/{conversation_id}/messages",
    tags=['Messages']
)

@router.post("/", response_model=MessageRead)
def create_message(message: MessageCreate, conversation_id: int, db: Session = Depends(get_db)):
    return message_service.create_message(db=db, conversation_id=conversation_id, content=message.content, role=MessageRole.USER)

@router.get("/", response_model=List[MessageRead])
def get_messages(conversation_id: int, db: Session = Depends(get_db)):
    return message_service.get_messages(db=db, conversation_id=conversation_id)