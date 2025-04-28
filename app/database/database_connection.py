from sqlmodel import SQLModel, create_engine, Session

class DatabaseConnection():
    def __init__(self,database_url:str, echo_status:bool=True):
        engine = create_engine(database_url,echo_status)
    
    def initialize_database(self):
        SQLModel.metadata.create_all(self.engine)
    
    def get_session(self):
        with Session(self.engine) as session:
            yield session