from sqlmodel import SQLModel,Session, select,col
from .database_models import User, Blog
from .database_connection import DatabaseConnection

class BlogDatabaseService:
    def __init__(self, database_url:str, echo_status:bool = True):
        self.conn: DatabaseConnection = DatabaseConnection(database_url)
        self.session: Session = next(self.conn.get_session())
        
    def create_blog(self, user_id, blog:Blog):
        user = self.session.get(User, user_id)
        blog = Blog(title=blog.title,
                    content=blog.content,
                    published_at=blog.published_at,
                    modified_at=blog.modified_at,
                    author_id=user_id,
                    author=user)
        self.session.add(blog)
        self.session.commit()
        self.session.refresh(blog)
        return blog
        
    def get_blogs(self)-> list[Blog]:
        blogs:list[Blog] = self.session.exec(select(Blog))
        return blogs
        
    def get_blog_by_id(self, blog_id)-> Blog:
        blog = self.session.get(Blog,blog_id)
        return blog
    
    def update_blog_title(self, blog_id, title)->Blog:
        blog:Blog = self.session.get(Blog)
        blog.title = title