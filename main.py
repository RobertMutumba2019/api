from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool=True
    rating: Optional[int]=None

my_posts=[{"title": "title of post 1", 
"content": "content of post 1", "id": 1 }]


@app.get("/")
def root():
    return {"Sun Systems": "Flaxem data"} 

@app.get("/posts") #decorators identifying the route of the app 
def get_posts():
    return {"data": my_posts}
    #return{"Sun connect": "Get that data"}

@app.post("/posts")
def create_posts(post:Post):
    my_posts.append(post.dict())
    return{"data": "new post"}
 