from fastapi import APIRouter

# ✅ Create a router instance
router = APIRouter()

# Dummy endpoint to test
@router.get("/ping")
def ping():
    return {"message": "Auth route is working!"}
