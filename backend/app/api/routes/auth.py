from fastapi import APIRouter, HTTPException

from backend.app.api.models.auth import LoginRequest
from backend.app.db.main import get_user_by_email

router = APIRouter()

@router.post("/login")
def login(request: LoginRequest):
    """ Authenticate user"""
    user = get_user_by_email(request.email)

    if user is None:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if user["user_pass"] != request.password:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"message": "Login successful"}