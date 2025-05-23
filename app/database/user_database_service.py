import uuid
from sqlmodel import Session, select, col
from .database_models import User
from .database_exceptions import DatabaseException


class UserDatabaseService():
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

    def create_user(self, user_model) -> User | None:
        if self.session.exec(select(User).where(col(User.first_name) == user_model.first_name)).first():
            return None
        try:
            user = User(user_name=user_model.user_name,
                        first_name=user_model.first_name,
                        last_name=user_model.last_name,
                        email=user_model.email,
                        password = user_model.password
                        )
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            print(e)
            raise DatabaseException("Failed to create user in database")

    def get_users(self) -> list[User]:
        try:
            users: list[User] = [
                user for user in self.session.exec(select(User))]
            return users
        except Exception as e:
            print(e)
            raise DatabaseException("Failed to read users from database.")

    def get_user_by_id(self, user_id: str) -> User | None:
        # Check wether user_id is a valid uuid
        if not UserDatabaseService.check_valid_uuid(user_id):
            return None
        try:
            user: User = self.session.get(User, user_id)
            if user:
                return user
            else:
                return None
        except Exception as e:
            print(e)
            raise DatabaseException("Failed to read user from database")
        
    def get_user_by_name(self, user_name:str):
        try:
            user: User = self.session.exec(select(User).where(col(User.user_name) == user_name)).first()
            return user
        except Exception as e:
            print(e)
            raise DatabaseException(f"Failed to retrieve user by user_name {user_name}")

    def update_user_full_name(self, user_id: str, full_name) -> User | None:
        # Check wether user_id is a valid uuid
        if not UserDatabaseService.check_valid_uuid(user_id):
            return None
        try:
            user: User = self.session.get(User, user_id)
            if user:
                user.first_name = full_name.first_name
                user.last_name = full_name.last_name
                self.session.add(user)
                self.session.commit()
                self.session.refresh(user)
                return user
            else:
                return None
        except Exception as e:
            print(e)
            raise DatabaseException(
                f"Failed to update user names for user with id {user_id}")

    def update_user_email(self, user_id: str, email: str) -> User | None:
        # Check wether user_id is a valid uuid
        if not UserDatabaseService.check_valid_uuid(user_id):
            return None
        try:
            user: User = self.session.get(User, user_id)
            if user:
                user.email = email
                self.session.add(user)
                self.session.commit()
                self.session.refresh(user)
                return user
            else:
                return None
        except Exception as e:
            print(e)
            raise DatabaseException(
                f"Failed to update email for user with id {user_id}")

    def delete_user(self, user_id) -> None:
        # Check wether user_id is a valid uuid
        if not UserDatabaseService.check_valid_uuid(user_id):
            return None
        try:
            user = self.session.get(User, user_id)
            self.session.delete(user)
            return self.session.get(User, user_id)
        except Exception as e:
            print(e)
            raise DatabaseException(
                "Failed to delete user with id {user_id} from database.")
