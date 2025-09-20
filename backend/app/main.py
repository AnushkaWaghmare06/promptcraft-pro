from fastapi import FastAPI
from app.api.v1 import routes_auth ,routes_prompt ,routes_project# import your router

app = FastAPI(title="PromptCraft Pro API")

# ✅ Include the router
app.include_router(routes_auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(routes_prompt.router, prefix="/api/v1/prompt", tags=["prompt"])
app.include_router(routes_project.router, prefix="/api/v1/projects", tags=["projects"])

@app.get("/")
def root():
    return {"message": "Backend is running!"}
