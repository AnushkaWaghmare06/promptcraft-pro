from fastapi import APIRouter, HTTPException
from app.services import deploy_service

router = APIRouter()

@router.post("/frontend")
def deploy_frontend(payload: dict):
    project_path = payload.get("project_path")
    provider = payload.get("provider", "vercel")
    if not project_path:
        raise HTTPException(status_code=400, detail="Project path required")

    result = deploy_service.deploy_frontend(project_path, provider)
    return {"deployment_result": result}

@router.post("/backend/docker")
def deploy_backend(payload: dict):
    project_path = payload.get("project_path")
    image_name = payload.get("image_name", "my-backend:latest")
    if not project_path:
        raise HTTPException(status_code=400, detail="Project path required")

    build_log = deploy_service.build_docker_image(project_path, image_name)
    push_log = deploy_service.push_docker_image(image_name)
    return {"build_log": build_log, "push_log": push_log}
