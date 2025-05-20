from fastapi import APIRouter, status, HTTPException
from app.api.api_models.response_models import UserResponse
from app.api.api_models.body_models import UserUpdateName, UserUpdateEmail
from app.database import DatabaseConnection, UserDatabaseService
from app.config.config import Settings, DATABASE_ENGINE

settings = Settings()
DATABASE_ENGINE = DatabaseConnection(settings.database_url).get_engine()

router = APIRouter(prefix="/user")


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_by_id(user_id: str):
    session = UserDatabaseService(DATABASE_ENGINE)
    user = session.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} does not exist")
    return user

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserResponse])
async def get_users():
    session = UserDatabaseService(DATABASE_ENGINE)
    users = session.get_users()
    return users
    

@router.patch("/name/{user_id},", status_code=status.HTTP_200_OK,response_model=UserResponse)
async def update_user_full_name(user_id: str, name: UserUpdateName):
    session = UserDatabaseService(DATABASE_ENGINE)
    user = session.update_user_full_name(user_id, name)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} does not exist")
    return user


@router.patch("/email/{user_id},", status_code=status.HTTP_200_OK,response_model=UserResponse)
async def update_user_email(user_id: str, email: UserUpdateEmail):
    session = UserDatabaseService(DATABASE_ENGINE)
    user = session.update_user_email(user_id, email.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} does not exist")
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str):
    session = UserDatabaseService(DATABASE_ENGINE)
    user = session.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} does not exist")
    