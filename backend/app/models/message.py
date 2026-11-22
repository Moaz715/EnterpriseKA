from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, func, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import MessageRole

class Message(Base):
    __tablename__ = "messages"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"), index=True)
    
    content: Mapped[str] = mapped_column(Text)
    
    role: Mapped[MessageRole] = mapped_column(Enum(MessageRole, name="message_role"))
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    conversation: Mapped["Conversation"] = relationship(back_populates="messages")