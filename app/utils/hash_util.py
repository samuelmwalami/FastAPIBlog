from passlib.context import CryptContext

class Hashing:
    def __init__(self) -> str:
        self.hash_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
    def get_hash_from_text(self,plain_password: str):
        return self.hash_context.hash(plain_password)
    
    def verify_password_from_hash(self, plain_password: str, hashed_password: str) -> str:
        return self.hash_context.verify(plain_password, hashed_password)