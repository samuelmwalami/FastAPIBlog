from sqlmodel import SQLModel, create_engine, Session
from .database_exceptions import DatabaseException

class DatabaseConnection():
    def __init__(self,database_url:str, echo_status:bool=True):
        self.engine = create_engine(database_url,echo=echo_status)
    
    def initialize_database(self):
        try:
            SQLModel.metadata.create_all(self.engine)
        except Exception as e:
            print(f"Error occurred {e}")
            raise DatabaseException("Failed to initialize database.")
    
    def get_session(self):
        with Session(self.engine) as session:
            yield session