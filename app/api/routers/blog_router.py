from fastapi import APIRouter,status, HTTPException
from app.api.api_models.response_models import BlogResponse
from app.api.api_models.body_models import BlogCreate, BlogUpdateContent, BlogUpdateTitle
from app.database import BlogDatabaseService
from app.config.config import DATABASE_ENGINE


dummy_user_id="b97530cb-6658-4d52-b2fc-afea521cdc86"

router = APIRouter(prefix="/blog", tags=["Blog"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BlogResponse)
async def create_blog(blog: BlogCreate):
    session = BlogDatabaseService(DATABASE_ENGINE)
    new_blog = session.create_blog(user_id=dummy_user_id,blog=blog)
    return new_blog

@router.get("/{blog_id}", status_code=status.HTTP_200_OK, response_model=BlogResponse)
async def get_blog(blog_id: str):
    session = BlogDatabaseService(DATABASE_ENGINE)
    blog = session.get_blog_by_id(blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with blog id {blog_id} does not exist")
    return blog

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[BlogResponse])
async def get_blogs()-> list:
    session = BlogDatabaseService(DATABASE_ENGINE)
    blogs = session.get_blogs()
    return blogs

@router.patch("/title/", status_code=status.HTTP_200_OK, response_model=BlogResponse)
async def update_blog_title(blog: BlogUpdateTitle):
    session = BlogDatabaseService(DATABASE_ENGINE)
    updated_blog = session.update_blog_title(blog_id=blog.blog_id,
                                             title=blog.title)
    if not updated_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with blog id {blog.blog_id} does not exist")
    return updated_blog

@router.patch("/content/", status_code=status.HTTP_200_OK, response_model=BlogResponse)
async def update_blog_content(blog: BlogUpdateContent):
    session = BlogDatabaseService(DATABASE_ENGINE)
    updated_blog = session.update_blog_content(blog_id=blog.blog_id,
                                             content=blog.content)
    if not updated_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with blog id {blog.blog_id} does not exist")
    return updated_blog

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_by_id(blog_id: str):
    session = BlogDatabaseService(DATABASE_ENGINE)
    deleted_blog = session.delete_blog_by_id(blog_id)
    if not deleted_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with blog id {blog_id} does not exist")
    