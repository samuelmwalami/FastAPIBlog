from fastapi import APIRouter,status, HTTPException, Depends
from app.api.api_models.response_models import BlogResponse
from app.api.api_models.body_models import BlogCreate, BlogUpdateContent, BlogUpdateTitle
from app.database import BlogDatabaseService
from app.config.config import DATABASE_ENGINE
from app.api.dependencies.oauth2_dependencies import get_user, decode_token




router = APIRouter(prefix="/blog", tags=["Blog"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BlogResponse)
async def create_blog(blog: BlogCreate, user = Depends(get_user)):
    session = BlogDatabaseService(DATABASE_ENGINE)
    new_blog = session.create_blog(user_id=user.name,blog=blog)
    return new_blog

@router.get("/{blog_id}", status_code=status.HTTP_200_OK, response_model=BlogResponse, dependencies=[Depends(decode_token)])
async def get_blog(blog_id: str):
    session = BlogDatabaseService(DATABASE_ENGINE)
    blog = session.get_blog_by_id(blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with blog id {blog_id} does not exist")
    return blog

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[BlogResponse])
async def get_blogs(user = Depends(get_user))-> list:
    session = BlogDatabaseService(DATABASE_ENGINE)
    blogs = session.get_blogs()
    return blogs

@router.patch("/title/", status_code=status.HTTP_200_OK, response_model=BlogResponse, dependencies=[Depends(decode_token)])
async def update_blog_title(blog: BlogUpdateTitle):
    session = BlogDatabaseService(DATABASE_ENGINE)
    updated_blog = session.update_blog_title(blog_id=blog.blog_id,
                                             title=blog.title)
    if not updated_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with blog id {blog.blog_id} does not exist")
    return updated_blog

@router.patch("/content/", status_code=status.HTTP_200_OK, response_model=BlogResponse, dependencies=[Depends(decode_token)])
async def update_blog_content(blog: BlogUpdateContent):
    session = BlogDatabaseService(DATABASE_ENGINE)
    updated_blog = session.update_blog_content(blog_id=blog.blog_id,
                                             content=blog.content)
    if not updated_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with blog id {blog.blog_id} does not exist")
    return updated_blog

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(decode_token)])
async def delete_blog_by_id(blog_id: str ):
    session = BlogDatabaseService(DATABASE_ENGINE)
    deleted_blog = session.delete_blog_by_id(blog_id)
    if not deleted_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with blog id {blog_id} does not exist")
    