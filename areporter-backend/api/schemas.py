from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    timestamp: datetime
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_anonymous: bool

    class Config:
        orm_mode = True
