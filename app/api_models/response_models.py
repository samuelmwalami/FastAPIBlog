from pydantic import BaseModel

class BlogResponse(BaseModel):
    blog_id: str
    title: str 
    content: str
    published_at: str
    modified_at: str
    author_id: str

class UserResponse(BaseModel):
    user_id: str
    user_name: str 
    first_name: str
    last_name: str
    email: str
    