from sqlmodel import SQLModel,Session, select,col
from .database_models import User
from .database_connection import DatabaseConnection
from .database_exceptions import DatabaseException

class UserDatabaseService():
    def __init__(self, database_url:str, echo_status:bool = True):
        conn: DatabaseConnection = DatabaseConnection(database_url)
        session: Session = next(conn.get_session())
        
    def database_create_user(self,user):
        try:
            new_user = User(user_name=user.user,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        email=user.email)
            self.session.add(new_user)
            self.session.commit()
            self.session.refresh(new_user)
            return new_user
        except:
            raise DatabaseException("Create user")
        
    def database_read_user(self,user_id):
        try:
            user = self.session.get(User,user_id)
            return user
        except:
            raise DatabaseException("Read user")
    
    def database_read_users(self,):
        try:
            users = self.session.exec(select(User))
            return users
        except:
            raise DatabaseException("Read users")
    

        
    def database_delete_user(self,user_id):
        try:
            user = self.session.get(User,user_id)
            self.session.delete(user)
        except:
            raise DatabaseException("Delete user")
        
        
