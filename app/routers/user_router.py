from fastapi import APIRouter, status
from app.api_models.response_models import UserResponse

router = APIRouter(prefix="/user")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def register_user():
    pass

@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_by_id(user_id):
    pass

@router.get("/", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_users():
    pass

