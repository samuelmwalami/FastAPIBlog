import uuid
from pydantic import BaseModel, EmailStr



class BlogResponse(BaseModel):
    id: uuid.UUID
    title: str 
    content: str
    published_at: str
    modified_at: str
    author_id: uuid.UUID
    
 

class UserResponse(BaseModel):
    id: uuid.UUID
    user_name: str 
    first_name: str
    last_name: str
    email: EmailStr
    
