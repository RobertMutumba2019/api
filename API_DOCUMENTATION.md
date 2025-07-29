# API Documentation

## Overview

This is a FastAPI-based web application that provides RESTful APIs for managing posts and basic web functionality. The application consists of two main modules:

- `main.py`: Core API functionality with post management
- `web.py`: Simple web endpoint

## Table of Contents

1. [Installation & Setup](#installation--setup)
2. [API Endpoints](#api-endpoints)
3. [Data Models](#data-models)
4. [Usage Examples](#usage-examples)
5. [Error Handling](#error-handling)

## Installation & Setup

### Prerequisites

- Python 3.7+
- FastAPI
- Pydantic
- Uvicorn (for running the server)

### Installation

```bash
pip install fastapi pydantic uvicorn
```

### Running the Application

#### Main Application (main.py)
```bash
uvicorn main:app --reload
```

#### Web Application (web.py)
```bash
uvicorn web:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Main Application (main.py)

#### 1. Root Endpoint

**GET /** 

Returns basic information about the application.

**Response:**
```json
{
  "Sun Systems": "Flaxem data"
}
```

**Example:**
```bash
curl -X GET "http://localhost:8000/"
```

---

#### 2. Get All Posts

**GET /posts**

Retrieves all posts from the system.

**Response:**
```json
{
  "data": [
    {
      "title": "title of post 1",
      "content": "content of post 1",
      "id": 1
    }
  ]
}
```

**Example:**
```bash
curl -X GET "http://localhost:8000/posts"
```

**Python Example:**
```python
import requests

response = requests.get("http://localhost:8000/posts")
posts = response.json()
print(posts)
```

---

#### 3. Create New Post

**POST /posts**

Creates a new post in the system.

**Request Body:**
- `title` (string, required): The title of the post
- `content` (string, required): The content of the post
- `published` (boolean, optional): Publication status (default: true)
- `rating` (integer, optional): Post rating (default: null)

**Response:**
```json
{
  "data": "new post"
}
```

**Example:**
```bash
curl -X POST "http://localhost:8000/posts" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My New Post",
    "content": "This is the content of my new post",
    "published": true,
    "rating": 5
  }'
```

**Python Example:**
```python
import requests

post_data = {
    "title": "My New Post",
    "content": "This is the content of my new post",
    "published": True,
    "rating": 5
}

response = requests.post("http://localhost:8000/posts", json=post_data)
result = response.json()
print(result)
```

### Web Application (web.py)

#### 1. Root Endpoint

**GET /**

Returns a simple message from the Flaxem Systems.

**Response:**
```json
{
  "message": "Flaxem Systems"
}
```

**Example:**
```bash
curl -X GET "http://localhost:8000/"
```

## Data Models

### Post Model

The `Post` model is defined using Pydantic and represents a blog post or article.

```python
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
```

**Fields:**

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `title` | string | Yes | - | The title of the post |
| `content` | string | Yes | - | The main content of the post |
| `published` | boolean | No | `true` | Whether the post is published |
| `rating` | integer | No | `null` | Optional rating for the post |

**Validation Rules:**
- `title`: Must be a non-empty string
- `content`: Must be a non-empty string
- `published`: Boolean value
- `rating`: Optional integer value

## Usage Examples

### Complete Workflow Example

```python
import requests
import json

# Base URL
BASE_URL = "http://localhost:8000"

# 1. Check if the API is running
response = requests.get(f"{BASE_URL}/")
print("API Status:", response.json())

# 2. Get existing posts
response = requests.get(f"{BASE_URL}/posts")
existing_posts = response.json()
print("Existing posts:", json.dumps(existing_posts, indent=2))

# 3. Create a new post
new_post = {
    "title": "Getting Started with FastAPI",
    "content": "FastAPI is a modern, fast web framework for building APIs with Python 3.7+",
    "published": True,
    "rating": 5
}

response = requests.post(f"{BASE_URL}/posts", json=new_post)
create_result = response.json()
print("Create result:", create_result)

# 4. Get updated posts list
response = requests.get(f"{BASE_URL}/posts")
updated_posts = response.json()
print("Updated posts:", json.dumps(updated_posts, indent=2))
```

### JavaScript/Frontend Example

```javascript
// Fetch all posts
async function getAllPosts() {
    try {
        const response = await fetch('http://localhost:8000/posts');
        const data = await response.json();
        console.log('Posts:', data);
        return data;
    } catch (error) {
        console.error('Error fetching posts:', error);
    }
}

// Create a new post
async function createPost(postData) {
    try {
        const response = await fetch('http://localhost:8000/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(postData)
        });
        const result = await response.json();
        console.log('Post created:', result);
        return result;
    } catch (error) {
        console.error('Error creating post:', error);
    }
}

// Usage
const newPost = {
    title: "JavaScript Integration",
    content: "This post was created using JavaScript fetch API",
    published: true,
    rating: 4
};

createPost(newPost);
getAllPosts();
```

## Error Handling

### Common HTTP Status Codes

- `200 OK`: Request successful
- `422 Unprocessable Entity`: Validation error (invalid request body)
- `500 Internal Server Error`: Server error

### Validation Errors

When sending invalid data to POST endpoints, you'll receive a 422 status code with detailed error information:

```json
{
  "detail": [
    {
      "loc": ["body", "title"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Example Error Handling

```python
import requests

try:
    # Invalid post data (missing required fields)
    invalid_post = {"published": True}
    
    response = requests.post("http://localhost:8000/posts", json=invalid_post)
    
    if response.status_code == 422:
        errors = response.json()
        print("Validation errors:", errors)
    elif response.status_code == 200:
        print("Success:", response.json())
    else:
        print(f"Unexpected error: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
```

## Interactive API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

These interfaces allow you to:
- View all available endpoints
- Test API calls directly from the browser
- See request/response schemas
- Download OpenAPI specification

## Development Notes

### Current Limitations

1. **In-Memory Storage**: Posts are stored in a Python list (`my_posts`) and will be lost when the server restarts
2. **No Authentication**: All endpoints are publicly accessible
3. **No Pagination**: The `/posts` endpoint returns all posts without pagination
4. **No Update/Delete**: Currently only supports creating and reading posts

### Recommended Improvements

1. **Database Integration**: Replace in-memory storage with a proper database
2. **Authentication**: Add user authentication and authorization
3. **CRUD Operations**: Implement UPDATE and DELETE operations for posts
4. **Pagination**: Add pagination support for large datasets
5. **Input Validation**: Add more comprehensive validation rules
6. **Error Handling**: Implement proper error handling and logging

## Configuration

### Environment Variables

Currently, the application doesn't use environment variables, but you may want to add:

```bash
# .env file
DATABASE_URL=sqlite:///./posts.db
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### Production Deployment

For production deployment, consider:

```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## Support

For questions or issues:
1. Check the interactive documentation at `/docs`
2. Review this documentation
3. Check server logs for error details

---

*Last updated: [Current Date]*
*API Version: 1.0*