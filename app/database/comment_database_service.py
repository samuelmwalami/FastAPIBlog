from fastapi import select, Session

class CommentDatabaseService:
    def __init__(self, engine):
        self.engine = engine
        self.session = next(self.get_session)
        
        
    def get_session(self):
        with Session(self.engine) as session:
            yield session
            
    def get_comments(blog_id: str):
        pass
    
    def get_comment_by_id(comment_id: str):
        pass
    
    def update_comment_by_id(comment_id: str):
        pass
    
    def delete_comment_by_id(comment_id: str):
        pass