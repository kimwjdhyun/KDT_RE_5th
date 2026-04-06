from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username : str
    password : str
    name : str
    email : str

class UserUpdate(BaseModel):
    name : str
    email : str

class PostCreate(BaseModel):
    authour : str
    content : str

class PostUpdate(BaseModel):
    content : str

class Post(BaseModel):
    id : int
    author : str
    content : str
    created_at : datetime