from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai import get_ai_response

app = FastAPI()


class AIRequest(BaseModel):
    message: str


class AIResponse(BaseModel):
    response: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/ai", response_model=AIResponse)
async def call_ai(request: AIRequest):
    try:
        response_content = await get_ai_response(request.message)
        return AIResponse(response=response_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
