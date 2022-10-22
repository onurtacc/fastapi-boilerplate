from fastapi import APIRouter

from app.api.v1.auth.router import router as auth_routes
from app.api.v1.user.router import router as user_routes

api_router = APIRouter()
api_router.include_router(auth_routes, prefix="/auth", tags=["auth"])
api_router.include_router(user_routes, prefix="/user", tags=["user"])
