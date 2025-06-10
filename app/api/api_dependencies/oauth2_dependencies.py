from datetime import timedelta
from typing import Annotated
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwt_util import JWTUtil
from app.utils.hash_util import Hashing
from app.database import UserDatabaseService, UserToken
from app.config.config import SETTINGS, DATABASE_ENGINE



OAuth_context2 = OAuth2PasswordBearer(tokenUrl="/auth/token")
hashing_context = Hashing()
jwt_context = JWTUtil(SETTINGS.jwt_algorithm,SETTINGS.jwt_secret,timedelta(minutes=30))



def get_user_from_database(user_id: str):
    user = UserDatabaseService(DATABASE_ENGINE).get_user_by_id(user_id)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            detail="User not found")
    return UserToken(id=user.id,
                     user_name=user.user_name,
                     first_name=user.first_name,
                     last_name=user.last_name,
                     email=user.email)

async def decode_token(token: Annotated[str, Depends(OAuth_context2)]):
    payload = jwt_context.get_dict_from_jwt(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid token")
    return payload

async def get_current_user(payload: Annotated[dict, Depends(decode_token)]):
    user_id = payload.get("sub")
    user = get_user_from_database(user_id)
    return user


def verify_jwt_id_matches_user_id(user_in_db_id, authenticated_user):
    if user_in_db_id != authenticated_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail={"message" : " You are not allowed to edit other user's details"})