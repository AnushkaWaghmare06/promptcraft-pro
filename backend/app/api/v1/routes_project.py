# backend/app/api/v1/routes_project.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate
from app.services import project_service

router = APIRouter()

@router.post("/create", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    # TODO: replace user_id in payload with current user id from JWT in production
    proj = project_service.create_project(db, user_id=payload.user_id, name=payload.name, description=payload.description, framework=payload.framework)
    return proj

@router.get("/user/{user_id}", response_model=List[ProjectResponse])
def list_projects_for_user(user_id: int, db: Session = Depends(get_db)):
    projects = project_service.get_projects_by_user(db, user_id=user_id)
    return projects

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    proj = project_service.get_project(db, project_id=project_id)
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    return proj

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, payload: ProjectUpdate, db: Session = Depends(get_db)):
    updated = project_service.update_project(db, project_id=project_id, name=payload.name, description=payload.description, framework=payload.framework)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    ok = project_service.delete_project(db, project_id=project_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Project not found")
    return None
