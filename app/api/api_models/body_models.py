from pydantic import BaseModel, EmailStr

class BlogCreate(BaseModel):
    title: str 
    content: str
    
class BlogUpdateTitle(BaseModel):
    blog_id: str
    title: str 
    
class BlogUpdateContent(BaseModel):
    blog_id: str
    content: str
    
class UserCreate(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class UserUpdateName(BaseModel):
    first_name: str
    last_name: str

    
class UserUpdateEmail(BaseModel):
    email: EmailStr
    
class UserUpdatePassword(BaseModel):
    email: EmailStr
    password: str