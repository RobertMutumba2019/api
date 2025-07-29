"""
FastAPI Blog Post Management API

This module provides a RESTful API for managing blog posts using FastAPI.
It includes endpoints for creating and retrieving posts, with data validation
using Pydantic models.

Author: Flaxem Systems
Version: 1.0
"""

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional

# Initialize FastAPI application instance
app = FastAPI(
    title="Blog Post Management API",
    description="A simple API for managing blog posts with CRUD operations",
    version="1.0.0"
)


class Post(BaseModel):
    """
    Pydantic model representing a blog post.
    
    This model defines the structure and validation rules for blog posts
    in the system. All posts must have a title and content, with optional
    publication status and rating.
    
    Attributes:
        title (str): The title of the blog post. Required field.
        content (str): The main content/body of the blog post. Required field.
        published (bool): Whether the post is published. Defaults to True.
        rating (Optional[int]): Optional numerical rating for the post. Defaults to None.
    
    Example:
        >>> post = Post(
        ...     title="My First Post",
        ...     content="This is the content of my first post",
        ...     published=True,
        ...     rating=5
        ... )
    """
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# In-memory storage for posts (Note: This will be lost on server restart)
# TODO: Replace with persistent database storage for production use
my_posts = [
    {
        "title": "title of post 1", 
        "content": "content of post 1", 
        "id": 1
    }
]


@app.get("/")
def root():
    """
    Root endpoint that returns basic application information.
    
    This endpoint serves as a health check and provides basic information
    about the Sun Systems application.
    
    Returns:
        dict: A dictionary containing system information.
        
    Example:
        GET /
        Response: {"Sun Systems": "Flaxem data"}
    """
    return {"Sun Systems": "Flaxem data"}


@app.get("/posts")  # Decorator identifying the route of the app 
def get_posts():
    """
    Retrieve all blog posts from the system.
    
    This endpoint returns all posts currently stored in the system.
    Posts are returned in a data wrapper for consistent API response format.
    
    Returns:
        dict: A dictionary containing all posts in the 'data' key.
        
    Response Format:
        {
            "data": [
                {
                    "title": "Post Title",
                    "content": "Post Content",
                    "id": 1
                },
                ...
            ]
        }
        
    Example:
        GET /posts
        Response: {"data": [{"title": "title of post 1", "content": "content of post 1", "id": 1}]}
    """
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    """
    Create a new blog post in the system.
    
    This endpoint accepts a Post object in the request body and adds it to
    the posts collection. The post data is validated using the Post model
    before being stored.
    
    Args:
        post (Post): A Post object containing the post data to be created.
                    Must include title and content. Published status and
                    rating are optional.
    
    Returns:
        dict: A confirmation message indicating successful post creation.
        
    Raises:
        422 Unprocessable Entity: If the post data doesn't match the Post model schema.
        
    Example:
        POST /posts
        Request Body:
        {
            "title": "My New Post",
            "content": "This is my post content",
            "published": true,
            "rating": 5
        }
        Response: {"data": "new post"}
        
    Note:
        The created post is added to the in-memory storage and will be lost
        when the server restarts. Consider implementing persistent storage
        for production use.
    """
    # Convert Pydantic model to dictionary and append to posts list
    my_posts.append(post.dict())
    return {"data": "new post"}
 