# # backend/app/main.py
# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from . import models, schemas


# from . import models, schemas
# from .database import SessionLocal, engine, Base
# from fastapi.middleware.cors import CORSMiddleware

# # Create tables if not exist
# Base.metadata.create_all(bind=engine)

# app = FastAPI(title="PromptCraft Pro Backend")

# # Allow frontend dev server origins
# origins = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # -------------------------
# # Health Check
# # -------------------------
# @app.get("/api/health")
# def health():
#     return {"status": "ok", "db": "connected"}

# # -------------------------
# # Project CRUD
# # -------------------------
# @app.post("/api/projects", response_model=schemas.Project)
# def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
#     db_project = models.Project(name=project.name, description=project.description or "")
#     db.add(db_project)
#     db.commit()
#     db.refresh(db_project)
#     return db_project

# @app.get("/api/projects", response_model=List[schemas.Project])
# def list_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return db.query(models.Project).offset(skip).limit(limit).all()

# @app.get("/api/projects/{project_id}", response_model=schemas.Project)
# def get_project(project_id: int, db: Session = Depends(get_db)):
#     proj = db.query(models.Project).filter(models.Project.id == project_id).first()
#     if not proj:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return proj

# @app.post("/api/generate-project", response_model=schemas.GenerateProjectResponse)
# def generate_project(data: dict, db: Session = Depends(get_db)):
#     prompt = data.get("prompt")
#     if not prompt:
#         raise HTTPException(status_code=400, detail="Prompt is required")

#     generated_name = f"Project from: {prompt[:20]}"
#     generated_desc = f"This project was generated based on the idea: {prompt}"

#     db_project = models.Project(name=generated_name, description=generated_desc)
#     db.add(db_project)
#     db.commit()
#     db.refresh(db_project)

#     return {"output": f"Generated project: {db_project.name}", "project": db_project}


# main.py
from fastapi import FastAPI
from app.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="PromptCraft Pro")

@app.get("/")
def root():
    return {"message": "Backend is running"}


from fastapi import FastAPI
from .database import Base, engine
from .routers import auth, projects, admin

app = FastAPI(title="PromptCraft Pro Backend")

# Create tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(admin.router)  # admin router will come next
