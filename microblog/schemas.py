from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from user.schemas import User


class PostBase(BaseModel):
    title: str
    text: str


class PostList(PostBase):
    id: int
    date: datetime
    # user: User


class PostSingle(PostList):
    children: List[PostBase]


class PostCreate(PostBase):
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True
