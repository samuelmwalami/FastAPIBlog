from fastapi import APIRouter

router = APIRouter(prefix="/comment", tags=["comments"])

@router.post("/{blog_id}")
def read_blog_comments(blog_id: str):
    pass

@router.post("/{blog_id}")
def create_blog_comment(blog_id: str):
    pass

@router.post("/{blog_id}")
def update_blog_comment(blog_id: str):
    pass

@router.post("/{blog_id}")
def delete_blog_comment(blog_id: str):
    pass

