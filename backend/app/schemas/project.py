# backend/app/schemas/project.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProjectCreate(BaseModel):
    user_id: int
    name: str
    description: Optional[str] = None
    framework: Optional[str] = "react-fastapi"

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    framework: Optional[str] = None

class ProjectResponse(BaseModel):
    id: int
    user_id: int
    name: str
    description: Optional[str]
    framework: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
