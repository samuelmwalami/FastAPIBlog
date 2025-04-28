from fastapi import APIRouter

router = APIRouter(prefix="/user")

@router.post("/")
async def register_user():
    pass

@router.get("/{user_id}")
async def get_user_by_id(user_id):
    pass

@router.get("/")
async def get_users():
    pass

