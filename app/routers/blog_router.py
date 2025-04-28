from fastapi import APIRouter,status
from app.api_models.response_models import BlogResponse

router = APIRouter(prefix="/blog")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BlogResponse)
async def create_blog():
    pass

@router.get("/{blog_id}", status_code=status.HTTP_200_OK, response_model=BlogResponse)
async def get_blog(blog_id:str):
    pass

@router.get("/", status_code=status.HTTP_200_OK, response_model=BlogResponse)
async def get_blogs()-> list:
    pass

@router.patch("/title/{blog_id}", status_code=status.HTTP_200_OK, response_model=BlogResponse)
async def update_blog_title(blog_id: str):
    pass

@router.patch("/content/{blog_id}", status_code=status.HTTP_200_OK, response_model=BlogResponse)
async def update_blog_content(blog_id: str):
    pass

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_by_id(blog_id: str):
    pass