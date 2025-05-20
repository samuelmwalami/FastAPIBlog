from fastapi import APIRouter, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from api.api_models.response_models import UserResponse
from api.api_models.body_models import UserCreate
from app.config.config import DATABASE_ENGINE
from app.database import UserDatabaseService

OAuth_context = OAuth2PasswordBearer(tokenUrl="register")

router = APIRouter(prefix="/auth")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def register_user(user: UserCreate):
    session = UserDatabaseService(DATABASE_ENGINE)
    new_user = session.create_user(user)
    if not new_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User name already taken")
    return new_user