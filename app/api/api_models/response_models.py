import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr



class BlogResponse(BaseModel):
    id: uuid.UUID 
    title: str 
    content: str 
    published_at: datetime 
    modified_at: datetime
    author_id: uuid.UUID 
    
 

class UserResponse(BaseModel):
    id: uuid.UUID
    user_name: str 
    first_name: str
    last_name: str
    email: EmailStr
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
    
