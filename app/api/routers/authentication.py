from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

OAuth_context = OAuth2PasswordBearer(tokenUrl="register")