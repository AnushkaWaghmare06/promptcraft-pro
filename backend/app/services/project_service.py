# backend/app/services/project_service.py
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.project import Project
from datetime import datetime

def create_project(db: Session, user_id: int, name: str, description: Optional[str] = None, framework: Optional[str] = "react-fastapi") -> Project:
    proj = Project(user_id=user_id, name=name, description=description, framework=framework, created_at=datetime.utcnow())
    db.add(proj)
    db.commit()
    db.refresh(proj)
    return proj

def get_project(db: Session, project_id: int) -> Optional[Project]:
    return db.query(Project).filter(Project.id == project_id).first()

def get_projects_by_user(db: Session, user_id: int) -> List[Project]:
    return db.query(Project).filter(Project.user_id == user_id).order_by(Project.created_at.desc()).all()

def update_project(db: Session, project_id: int, **updates) -> Optional[Project]:
    proj = db.query(Project).filter(Project.id == project_id).first()
    if not proj:
        return None
    for key, value in updates.items():
        if value is not None and hasattr(proj, key):
            setattr(proj, key, value)
    db.commit()
    db.refresh(proj)
    return proj

def delete_project(db: Session, project_id: int) -> bool:
    proj = db.query(Project).filter(Project.id == project_id).first()
    if not proj:
        return False
    db.delete(proj)
    db.commit()
    return True
