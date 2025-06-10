from pydantic import BaseModel
import uuid


class UserToken(BaseModel):
    id: uuid.UUID 
    user_name: str 
    first_name: str
    last_name: str
    email: str
    