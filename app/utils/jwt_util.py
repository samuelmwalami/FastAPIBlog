from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

class JWTUtil:
    def __init__(self,algorithm:str, secret: str, expires_delta:timedelta) -> None:
        self.algorithm = algorithm
        self.secret = secret
        self.expires_delta = expires_delta
        
    def get_token_from_dict(self, payload: dict) -> str:
        to_update = payload.copy()
        to_update.update({"exp": datetime.now(timezone.utc) + self.expires_delta})
        token = jwt.encode(to_update, self.secret, self.algorithm)
        return token
    
    def get_dict_from_jwt(self, token) -> dict | None:
        try:
            payload = jwt.decode(token, self.secret, self.algorithm)
            return payload
        except JWTError as e:
            print(e)
            return None