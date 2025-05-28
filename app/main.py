from fastapi import FastAPI
from app.api.routers import blog_router, user_router, auth_router
from app.database import DatabaseConnection
from app.config.config import DATABASE_ENGINE



app = FastAPI()
@app.on_event("startup")
def on_startup():
    DatabaseConnection.initialize_database(DATABASE_ENGINE)
    
app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(auth_router.router)