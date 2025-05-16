from sqlmodel import SQLModel, Field, Relationship
import uuid
from datetime import datetime, timezone

class User(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    user_name: str = Field(index=True, unique=True)
    first_name: str
    last_name: str
    email: str
    
    blogs: list["Blog"] | None = Relationship(back_populates="author")


class Blog(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True,default_factory=uuid.uuid4)
    title: str = Field(index=True)
    content: str
    published_at: datetime = Field(default=datetime.now(timezone.utc))
    modified_at: datetime = Field(default=datetime.now(timezone.utc))
    
    author_id: uuid.UUID = Field(default_factory=uuid.uuid4, foreign_key="user.id")
    author: User = Relationship(back_populates="blogs")