from pydantic_settings import BaseSettings, SettingsConfigDict
from app.database import DatabaseConnection

# ENVIRONMENT VARIABLE
class Settings(BaseSettings):
    database_url: str
    jwt_algorithm: str
    jwt_secret: str
    
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8"
    )
    

# DATABASE SETTINGS    
# Database connection engine to be used by the entire application
SETTINGS = Settings()
DATABASE_ENGINE = DatabaseConnection(Settings().database_url).get_engine()