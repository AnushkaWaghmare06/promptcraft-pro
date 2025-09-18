from fastapi import FastAPI
from app.api.v1 import routes_auth ,routes_prompt # import your router

app = FastAPI(title="PromptCraft Pro API")

# ✅ Include the router
app.include_router(routes_auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(routes_prompt.router, prefix="/api/v1/prompt", tags=["prompt"])

@app.get("/ping")
def root():
    return {"message": "Backend is running!"}
