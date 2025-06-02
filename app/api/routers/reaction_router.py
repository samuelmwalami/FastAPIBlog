from fastapi import APIRouter

router = APIRouter(prefix="/reaction",tags=["Reaction"])

@router.post("/like/{blog_id}")
def like_blog(blog_id: str):
    pass

@router.post("/dislike/{blog_id}")
def dislike_blog(blog_id: str):
    pass