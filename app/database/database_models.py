from sqlmodel import SQLModel, Field, Relationship
import uuid

class User(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uui4)
    user_name: str = Field(index=True)
    first_name: str
    last_name: str
    email: str
    blogs: list["Blog"] | None = Relationship(back_populates="blog.author_id")


class Blog(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True,default_factory=uuid.uuid4)
    title: str = Field(index=True)
    content: str
    published_at: str
    modified_at: str
    
    author_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    author: User = Relationship(back_populates="user.blogs")