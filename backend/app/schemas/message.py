from datetime import datetime

from pydantic import BaseModel

from app.models.enums import MessageRole


class MessageCreate(BaseModel):
    content: str

class MessageRead(BaseModel):
    id: int
    content: str
    role: MessageRole
    created_at: datetime

    model_config = {"from_attributes": True}