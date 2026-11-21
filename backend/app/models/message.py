from typing import Literal
from enum import StrEnum

class MessageRole(StrEnum):
    USER = "user"
    SYSTEM = "system"

class Message():
    __tablename__ = "messages"
    
    content: str
    files: list[str]
    role: Literal[MessageRole.USER, MessageRole.SYSTEM] = MessageRole.USER