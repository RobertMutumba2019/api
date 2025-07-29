# Flaxem Systems - FastAPI Blog Management API

A modern, fast, and simple blog post management API built with FastAPI. This project provides RESTful endpoints for creating and managing blog posts with data validation and automatic API documentation.

## 🚀 Features

- **Fast & Modern**: Built with FastAPI for high performance and modern Python features
- **Data Validation**: Automatic request/response validation using Pydantic models
- **Interactive Documentation**: Auto-generated Swagger UI and ReDoc documentation
- **Type Safety**: Full type hints for better development experience
- **Async Support**: Asynchronous request handling for better performance
- **Easy Deployment**: Simple deployment options for development and production

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Deployment](#deployment)
- [Contributing](#contributing)

## ⚡ Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the main application:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Access the API:**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## 📁 Project Structure

```
flaxem-systems/
├── main.py              # Main API application with post management
├── web.py               # Simple web interface
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── API_DOCUMENTATION.md # Comprehensive API documentation
├── venv/               # Virtual environment (not in version control)
└── __pycache__/        # Python cache files (not in version control)
```

## 📚 API Documentation

### Main Application Endpoints (main.py)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Health check and basic info |
| GET    | `/posts` | Retrieve all blog posts |
| POST   | `/posts` | Create a new blog post |

### Web Application Endpoints (web.py)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Simple system message |

For detailed API documentation with examples, see [API_DOCUMENTATION.md](API_DOCUMENTATION.md).

## 🛠 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd flaxem-systems
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

### Running the Applications

#### Main Blog API (Recommended)
```bash
uvicorn main:app --reload
```

#### Simple Web Interface
```bash
uvicorn web:app --reload --port 8001
```

### API Examples

#### Create a New Post
```bash
curl -X POST "http://localhost:8000/posts" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is the content of my first blog post",
    "published": true,
    "rating": 5
  }'
```

#### Get All Posts
```bash
curl -X GET "http://localhost:8000/posts"
```

### Python Client Example

```python
import requests

# Base URL
BASE_URL = "http://localhost:8000"

# Create a new post
post_data = {
    "title": "Getting Started with FastAPI",
    "content": "FastAPI is amazing for building APIs quickly!",
    "published": True,
    "rating": 5
}

response = requests.post(f"{BASE_URL}/posts", json=post_data)
print("Created:", response.json())

# Get all posts
response = requests.get(f"{BASE_URL}/posts")
print("All posts:", response.json())
```

## 🔧 Development

### Code Structure

- **main.py**: Contains the main FastAPI application with post management functionality
- **web.py**: Contains a simple web interface endpoint
- **Post Model**: Pydantic model for data validation with fields:
  - `title` (required): Post title
  - `content` (required): Post content
  - `published` (optional): Publication status (default: True)
  - `rating` (optional): Numerical rating

### Development Features

- **Hot Reload**: Use `--reload` flag for automatic code reloading
- **Interactive Testing**: Use the built-in Swagger UI at `/docs`
- **Type Checking**: Full type hints for better IDE support
- **Data Validation**: Automatic request/response validation

### Running Tests

Currently, the project doesn't include tests, but you can add them using pytest:

```bash
pip install pytest pytest-asyncio httpx
# Add your tests in a tests/ directory
pytest
```

## 🚀 Deployment

### Development Deployment
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Production Deployment

#### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

#### Using Docker (create Dockerfile)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## ⚠️ Current Limitations

1. **In-Memory Storage**: Posts are stored in memory and lost on restart
2. **No Authentication**: All endpoints are publicly accessible
3. **Limited CRUD**: Only Create and Read operations are implemented
4. **No Pagination**: All posts are returned at once

## 🔮 Future Improvements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User authentication and authorization
- [ ] Full CRUD operations (Update, Delete)
- [ ] Pagination and filtering
- [ ] File upload support
- [ ] Caching layer
- [ ] Rate limiting
- [ ] Comprehensive test suite
- [ ] Docker containerization
- [ ] CI/CD pipeline

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions, issues, or support:

1. Check the [API Documentation](API_DOCUMENTATION.md)
2. Visit the interactive docs at `/docs` when running the application
3. Open an issue in the repository
4. Contact: Flaxem Systems

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Data validation by [Pydantic](https://pydantic-docs.helpmanual.io/)
- Served by [Uvicorn](https://www.uvicorn.org/)

---

**Made with ❤️ by Flaxem Systems**