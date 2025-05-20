from pydantic_settings import BaseSettings, SettingsConfigDict
from app.database import DatabaseConnection

# ENVIRONMENT VARIABLE
class Settings(BaseSettings):
    database_url: str
    
    model_config = SettingsConfigDict(
        env_file = "app/config/.env",
        env_file_encoding = "utf-8"
    )
    

# DATABASE SETTINGS    
# Database connection engine to be used by the entire application
DATABASE_ENGINE = DatabaseConnection(Settings().database_url).get_engine()