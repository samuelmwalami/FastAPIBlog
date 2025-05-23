from fastapi import FastAPI
from app.api.routers import blog_router, user_router, auth_router

app = FastAPI()

app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(auth_router.router)