from sqlmodel import SQLModel, create_engine
from .database_exceptions import DatabaseException

# class that creates a database connection that will be used to generate sessions
class DatabaseConnection():
    def __init__(self, database_url:str, echo_status:bool=True):
        self.database_url = database_url
        self.echo_status = echo_status
    
    #Creates database and tables
    def initialize_database(self):
        try:
            print("Initializing Database with tables")
            SQLModel.metadata.create_all(self.get_engine())
            print("Created database and tables")
        except Exception as e:
            print(e)
            raise DatabaseException("Failed to initialize database.")
        
    def get_engine(self):
        return create_engine(self.database_url, echo = self.echo_status)