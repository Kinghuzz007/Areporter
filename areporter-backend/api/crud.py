from sqlalchemy.orm import Session
from . import models, schemas

def create_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(content=post.content, owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).order_by(models.Post.timestamp.desc()).offset(skip).limit(limit).all()
