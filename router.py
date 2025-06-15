from fastapi import APIRouter
from models import chatrequest, chatresponse
from chat import get_gemini_response

router = APIRouter()

@router.post("/chat", response_model=chatresponse)
async def chat_endpoint(request:chatrequest):
    reply = get_gemini_response(request.message)
    return {"reply":reply}