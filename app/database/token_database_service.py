from sqlmodel import Session, select, col
from .database_models import AccessToken, User

class TokenDatabaseService:
    def __init__(self, database_engine):
        self.engine = database_engine
        self.session = next(self.get_Session())
       
        
    def get_Session(self):
        with Session(self.engine) as session:
            yield session
            
            
    def store_token(self, user_id, token):
        token_in_db = self.session.exec(select(AccessToken).where(col(AccessToken.user_id) == user_id)).first()
        if token_in_db:
            return token_in_db    
        access_token: AccessToken = AccessToken(token=token,
                                                user_id=user_id)
        self.session.add(access_token)
        self.session.commit()
        self.session.refresh(access_token)
        return access_token
    
    def get_token(self, token):
        access_token = self.session.exec(select(AccessToken).where(col(AccessToken.token) == token)).first()
        return access_token
            
        
    def delete_token(self, token):
        access_token = self.session.exec(select(AccessToken).where(col(AccessToken.token) == token)).first()
        if access_token:
            self.session.delete(access_token)
            self.session.commit()
            return None