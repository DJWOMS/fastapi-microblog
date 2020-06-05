import uuid
from typing import Optional

import pydantic
from fastapi_users import models
from pydantic import EmailStr, BaseModel


class User(models.BaseUser):

    class Config:
        orm_mode = True


class UserInPost(BaseModel):
    id: Optional[str]
    name: str = None

    @pydantic.validator("id", pre=True, always=True)
    def default_id(cls, v):
        return v or str(uuid.uuid4())

    class Config:
        orm_mode = True


class UserCreate(User, models.BaseUserCreate):
    name: str


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass

