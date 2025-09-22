# routes_prompt.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services import ai_service

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str
    frontend_framework: str = "react-tailwind"
    backend_framework: str = "fastapi"

class PromptResponse(BaseModel):
    frontend_code: str
    backend_code: str

@router.post("/", response_model=PromptResponse)
def generate_code(request: PromptRequest):
    result = ai_service.generate_code(
        prompt=request.prompt,
        frontend_framework=request.frontend_framework,
        backend_framework=request.backend_framework
    )
    return result
