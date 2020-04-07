from sqlalchemy.orm import Session
from .models import Post
from .schemas import PostCreate


def get_post_list(db: Session):
    return db.query(Post).all()


def create_post(db: Session, item: PostCreate):
    post = Post(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
