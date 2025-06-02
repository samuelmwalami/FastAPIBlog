import uuid
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone

class User(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    user_name: str = Field(index=True, unique=True)
    first_name: str
    last_name: str
    email: str
    password: str = Field(index=True)
    
    blogs: list["Blog"] | None = Relationship(back_populates="author")
    
   
    access_token: Optional["AccessToken"] = Relationship(back_populates="user")
    
    comments: list["Comment"] | None = Relationship(back_populates="user")
    
    reactions: list["Reaction"] | None = Relationship(back_populates="user")


class Blog(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True,default_factory=uuid.uuid4)
    title: str = Field(index=True)
    content: str
    published_at: datetime = Field(default=datetime.now(timezone.utc))
    modified_at: datetime = Field(default=datetime.now(timezone.utc))
    
    author_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    author: User = Relationship(back_populates="blogs")
    
    comments: list["Comment"] | None = Relationship(back_populates="blog")
    
    reactions: list["Reaction"] | None = Relationship(back_populates="blog")
    
    


class AccessToken(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    token: str = Field(index=True, unique=True)
    
    user_id: uuid.UUID = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="access_token")
    
class Comment(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    content: str = Field(index=True)
    
    user_id: uuid.UUID = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="comments")
    
    blog_id: uuid.UUID = Field(foreign_key="blog.id")
    blog: Blog = Relationship(back_populates="comments")
    
class Reaction(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    reaction: str = Field(index=True)
    
    user_id: uuid.UUID = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="reactions")
    
    blog_id: uuid.UUID = Field(foreign_key="blog.id")
    blog: "Blog" = Relationship(back_populates="reactions")
    