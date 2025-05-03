from sqlmodel import Session, select
from .database_models import User
from .database_connection import DatabaseConnection
from .database_exceptions import DatabaseException

class UserDatabaseService():
    def __init__(self, database_url:str, echo_status:bool = True):
        self.conn: DatabaseConnection = DatabaseConnection(database_url)
        self.session: Session = next(self.conn.get_session())
        
    def create_user(self,user) -> User:
        try:
            user = User(user_name=user.user_name,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        email=user.email
                        )
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            print(e)
            raise DatabaseException("Failed to create user in database")
        
    def read_users(self) -> list[User]:
        try:
            users = self.session.exec(select(User))
            return users
        except Exception as e:
            print(e)
            raise DatabaseException("Failed to read users from database.")
        
    def read_user(self, user_id: str) -> User | None:
        try:
            user: User = self.session.get(User,user_id)
            if user:
                return user
            else: 
                return None
        except Exception as e:
            print(e)
            raise DatabaseException("Failed to read user from database")
        
    def update_user_first_name(self, user_id: str, first_name: str) -> User | None :
        try:
            user: User = self.session.get(User, user_id)
            if user:
                user.first_name = first_name
                self.session.add(user)
                self.session.commit()
                self.session.refresh(user)
                return User
            else:
                return None
        except Exception as e:
            print(e)
            raise DatabaseException(f"Failed to update first name for user with id {user_id}")
    
    def update_user_last_name(self, user_id: str, last_name: str) -> User | None :
        try:
            user: User = self.session.get(User, user_id)
            if user:
                user.last_name = last_name
                self.session.add(user)
                self.session.commit()
                self.session.refresh(user)
                return User
            else:
                return None
        except Exception as e:
            print(e)
            raise DatabaseException(f"Failed to update last name for user with id {user_id}")
    
    def update_user_email(self, user_id: str, email: str) -> User | None:
        try:
            user: User = self.session.get(User, user_id)
            if user:
                user.email = email
                self.session.add(user)
                self.session.commit()
                self.session.refresh(user)
                return User
            else:
                return None
        except Exception as e:
            print(e)
            raise DatabaseException(f"Failed to update email for user with id {user_id}")
    
    def database_delete_user(self,user_id) -> None:
        try:
            user = self.session.get(User, user_id)
            self.session.delete(user)
            if not self.session.get(user_id):
                return None
        except Exception as e:
            print(e)
            raise DatabaseException("Failed to delete user with id {user_id} from database.")
        
        
