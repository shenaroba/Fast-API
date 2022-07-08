from datetime import datetime
from lib2to3.pgen2.token import OP
from typing import Text
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime

app = FastAPI()

posts = []

#post model
class Post(BaseModel):
    id:Optional[str]
    title:str
    autor:str
    content: Text
    createt_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


@app.get('/')
def read_root():
    return{"welcome": "Welcome to my API"}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    print(post)
    return "recivido"
