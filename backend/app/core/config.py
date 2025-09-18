from backend.app.schemas.schemas import ProjectRequest, ProjectResponse

def generate_project(payload: ProjectRequest) -> ProjectResponse:
    # Dummy project generation logic (later connect to AI model)
    return ProjectResponse(
        project_name="demo_project",
        description=f"Generated project from prompt: {payload.prompt}",
        files={
            "main.py": "print('Hello from generated project!')"
        }
    )
