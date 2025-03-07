from fastapi import FastAPI, HTTPException
from models import ChatRequest
from services import process_chat

app = FastAPI()

@app.post("/chat")
async def chat(request: ChatRequest):
    result = process_chat(request.message)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result
