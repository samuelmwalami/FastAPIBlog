from sqlmodel import Session, select
from .database_models import User, Blog
from .database_connection import DatabaseConnection
from .database_exceptions import DatabaseException

class BlogDatabaseService:
    def __init__(self, database_url:str, echo_status:bool = True):
        self.conn: DatabaseConnection = DatabaseConnection(database_url)
        self.session: Session = next(self.conn.get_session())
        
    def create_blog(self, user_id: str, blog: Blog):
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
        
    def get_blog_by_id(self, blog_id: str)-> Blog:
        try:
            blog = self.session.get(Blog,blog_id)
            return blog
        except:
            raise DatabaseException(f"Failed to get user by id {blog_id}")
    
    def update_blog_title(self, blog_id: str, title) -> Blog | None:
        try:
            blog: Blog = self.session.get(Blog, blog_id)
            if blog:
                blog.title = title
                self.session.add(blog)
                self.session.commit(blog)
                self.session.refresh(blog)
                return blog
            else:
                return None
        except:
            raise DatabaseException(f"Failed to update blog title for blog with id {blog_id}")
    
    def update_blog_content(self, blog_id: str, content: str) -> Blog | None:
        try:
            blog: Blog = self.session.get(Blog, blog_id)
            if blog:
                blog.content = content
                self.session.add(blog)
                self.session.commit()
                self.session.refresh(blog)
                return blog
            else:
                return None
        except:
            raise DatabaseException(f"Failed to update blog content with blog id {blog_id}")
        
    def delete_blog_by_id(self, blog_id: str) -> Blog:
        try:
            blog: Blog = self.session.get(Blog, blog_id)
            self.session.delete(blog)
            self.session.commit()
            if not self.session.get(Blog):
                return f"Blog with blog id {blog_id} deleted successfully"
        except:
            raise DatabaseException(f"Failed to delete blog with blog id {blog_id}")
        