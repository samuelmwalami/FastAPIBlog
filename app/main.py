from fastapi import FastAPI
from app.api.routers import blog_router, user_router, auth_router
from app.database import DatabaseConnection
from app.config.config import SETTINGS




app = FastAPI()
@app.on_event("startup")
def on_startup():
    DatabaseConnection(database_url=SETTINGS.database_url, echo_status=True).initialize_database()

@app.get("/")
async def home():
    return{"Welcome": "Welcome to Blog API"}
    
app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(auth_router.router)