from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from app.database import DatabaseConnection

# ENVIRONMENT VARIABLE
class Settings(BaseSettings):
    database_url: str = Field(..., alias="DATABASE_URL")
    jwt_algorithm: str = Field(..., alias="JWT_ALGORITHM")
    jwt_secret: str = Field(..., alias="JWT_SECRET")
    
    # model_config = SettingsConfigDict(
    #     env_file = ".env",
    #     env_file_encoding = "utf-8"
    # )
    

# DATABASE SETTINGS    
# Database connection engine to be used by the entire application
SETTINGS = Settings()
DATABASE_ENGINE = DatabaseConnection(Settings().database_url).get_engine()