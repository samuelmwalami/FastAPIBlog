from fastapi import APIRouter, status
from app.api.api_models.response_models import UserResponse
from app.api.api_models.body_models import UserCreate, UserUpdateName
from app.database import DatabaseConnection, UserDatabaseService
from app.config.config import Settings

settings = Settings()
DATABASE_ENGINE = DatabaseConnection(settings.database_url).get_engine()

router = APIRouter(prefix="/user")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def register_user(user: UserCreate):
    session = UserDatabaseService(DATABASE_ENGINE)
    new_user = session.create_user(user)
    return new_user


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_by_id(user_id: str):
    session = UserDatabaseService(DATABASE_ENGINE)
    user = session.get_user_by_id(user_id)
    return user

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserResponse])
async def get_users():
    session = UserDatabaseService(DATABASE_ENGINE)
    users = session.get_users()
    return users
    

@router.patch("/{user_id},", status_code=status.HTTP_200_OK,response_model=UserResponse)
async def update_user_full_name(user_id: str, name: UserUpdateName):
    session = UserDatabaseService(DATABASE_ENGINE)
    user = session.update_user_full_name(user_id, name)
    return user


@router.patch("/,", status_code=status.HTTP_200_OK,response_model=UserResponse)
async def update_user_email(user_id: str, name: UserUpdateName):
    session = UserDatabaseService(DATABASE_ENGINE)
    user = session.update_user_last_name(user_id, name.name)
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str):
    session = UserDatabaseService(DATABASE_ENGINE)
    user = session.delete_user(user_id)
    