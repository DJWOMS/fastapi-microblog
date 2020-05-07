from typing import List
from fastapi import APIRouter, Depends
from core.fast_users import fastapi_users
from user.models import User
from . import service
from . schemas import PostCreate, PostList


router = APIRouter()


@router.get("/", response_model=List[PostList])
async def post_list():
    return await service.get_post_list()


@router.post("/")
async def post_create(item: PostCreate, user: User = Depends(fastapi_users.get_current_active_user)):
    return await service.create_post(item, user)
