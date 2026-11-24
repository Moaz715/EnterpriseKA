from fastapi import APIRouter

from app.apis import user, conversation, message

api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(conversation.router)
api_router.include_router(message.router)