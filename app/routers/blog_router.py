from fastapi import APIRouter,status

router = APIRouter(prefix="/blog")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_blog():
    pass

@router.get("/{blog_id}", status_code=status.HTTP_200_OK)
async def get_blog(blog_id:str):
    pass

@router.get("/", status_code=status.HTTP_200_OK)
async def get_blogs()-> list:
    pass

@router.patch("/title/{blog_id}", status_code=status.HTTP_200_OK)
async def update_blog_title(blog_id: str):
    pass

@router.patch("/content/{blog_id}", status_code=status.HTTP_200_OK)
async def update_blog_content(blog_id: str):
    pass

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog_by_id(blog_id: str):
    pass