from user.models import User
from .models import posts
from .schemas import PostCreate
from core.db import database


async def get_post_list():
    return await database.fetch_all(query=posts.select())


async def create_post(item: PostCreate, user: User):
    post = posts.insert().values(**item.dict(), user=user.id)
    return await database.execute(post)
