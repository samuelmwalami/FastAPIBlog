from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, status, HTTPException, Depends,Body
from fastapi.security import OAuth2PasswordRequestForm
from app.api.api_models.response_models import UserResponse, Token
from app.api.api_models.body_models import UserCreate, UserUpdatePassword
from app.config.config import DATABASE_ENGINE, SETTINGS
from app.database import UserDatabaseService, UserToken
from app.utils.hash_util import Hashing
from app.utils.jwt_util import JWTUtil
from app.api.api_dependencies.oauth2_dependencies import get_current_user

hashing_context = Hashing()
jwt_context = JWTUtil(SETTINGS.jwt_algorithm,SETTINGS.jwt_secret,timedelta(minutes=30))

router = APIRouter(prefix="/auth", tags=["Authentication"])
   


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def register_user(user: UserCreate):
    session = UserDatabaseService(DATABASE_ENGINE)
    user.password = hashing_context.get_hash_from_text(user.password)
    new_user = session.create_user(user)
    if not new_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User name already taken")
    return new_user

@router.post("/token", status_code=status.HTTP_200_OK)
#async def login_for_token(email: Annotated[str, Body()], password: Annotated[str, Body()]):
async def login_for_token(login_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    email = login_data.username
    password = login_data.password
    
    session = UserDatabaseService(DATABASE_ENGINE)
    user = session.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail= "Invalid Credentials",
                            headers = {"WWW-Authenticate" : "Bearer"})
    
    if not hashing_context.verify_password_from_hash(plain_password=password, hashed_password=user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials",
                            headers={"WWW-Authenticate" : "Bearer"})
    
    payload = {"sub" : str(user.id),
               "name" : user.user_name
               }
    token = jwt_context.get_token_from_dict(payload)
    return Token(access_token=token, token_type="Bearer")


@router.get("/me",status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_current_user(user: Annotated[UserToken, Depends(get_current_user)]):
    print(user.id)
    return user

@router.post("/reset",status_code=status.HTTP_200_OK, response_model=UserResponse)
async def reset_password(details: UserUpdatePassword):
    session = UserDatabaseService(DATABASE_ENGINE)
    hashed_password = hashing_context.get_hash_from_text(details.password)
    user = session.update_user_password(details.email, hashed_password)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid email")
        
    return user