import uuid
from datetime import datetime,timezone
from sqlmodel import Session, select
from .database_models import User, Blog
from .database_exceptions import DatabaseException
from .user_database_service import UserDatabaseService

class BlogDatabaseService:
    def __init__(self, database_engine):
        self.engine = database_engine
        self.session: Session = next(self.get_session())
        
    @staticmethod
    def check_valid_uuid(blog_id):
        try:
            if uuid.UUID(blog_id):
                return True
        except ValueError:
            return False
        
    def get_session(self):
        with Session(self.engine) as session:
            yield session
    
    def create_blog(self, user_id: str, blog):
        # get user from database
        user = UserDatabaseService(self.engine).get_user_by_id(user_id)    
        if user and user == type(User):    
            blog = Blog(title=blog.title,
                    content=blog.content,
                    author=user)
            self.session.add(blog)
            self.session.commit()
            self.session.refresh(blog)
            return blog
        else:
            return None
        
    def get_blogs(self)-> list[Blog]:
        blogs:list[Blog] = [blog for blog in self.session.exec(select(Blog))]
        return blogs
        
    def get_blog_by_id(self, blog_id: str)-> Blog | None:
        # Check wether blog_id is a valid uuid
        if not BlogDatabaseService.check_valid_uuid(blog_id):
            return None
        try:
            blog = self.session.get(Blog, uuid.UUID(blog_id))
            return blog
        except Exception as e:
            print(e)
            raise DatabaseException(f"Failed to get blog by id {blog_id}")
    
    def update_blog_title(self, blog_id: str, title: str) -> Blog | None:
        # Check wether blog_id is a valid uuid
        if not BlogDatabaseService.check_valid_uuid(blog_id):
            return None

        try:
            blog: Blog = self.session.get(Blog, blog_id)
            if blog:
                blog.title = title
                blog.modified_at = datetime.now(timezone.utc)
                self.session.add(blog)
                self.session.commit()
                self.session.refresh(blog)
            return blog
        except Exception as e:
            print(e)
            raise DatabaseException(f"Failed to update blog title for blog with id {blog_id}")
    
    def update_blog_content(self, blog_id: str, content: str) -> Blog | None:
        # Check wether blog_id is a valid uuid
        if not BlogDatabaseService.check_valid_uuid(blog_id):
            return None       
        
        try:
            blog: Blog = self.session.get(Blog, blog_id)
            if blog:
                blog.content = content
                self.session.add(blog)
                self.session.commit()
                self.session.refresh(blog)
            return blog
           
        except:
            raise DatabaseException(f"Failed to update blog content with blog id {blog_id}")
        
    def delete_blog_by_id(self, blog_id: str) -> Blog | None:
        # Check wether blog_id is a valid uuid
        if not BlogDatabaseService.check_valid_uuid(blog_id):
            return None
        
        try:
            blog: Blog = self.session.get(Blog, blog_id)
            if blog:
                self.session.delete(blog)
                self.session.commit()
            return self.session.get(Blog, blog_id)
        except:
            raise DatabaseException(f"Failed to delete blog with blog id {blog_id}")
        