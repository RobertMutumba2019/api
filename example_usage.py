#!/usr/bin/env python3
"""
Example Usage Script for Flaxem Systems FastAPI Blog Management API

This script demonstrates how to interact with the blog post management API
programmatically using the requests library. It shows examples of all
available operations.

Prerequisites:
- The FastAPI server should be running (uvicorn main:app --reload)
- Install requests: pip install requests

Author: Flaxem Systems
Version: 1.0
"""

import requests
import json
import time
from typing import Dict, Any, Optional


class BlogAPIClient:
    """
    A simple client for interacting with the Blog Management API.
    
    This class provides methods to interact with all available endpoints
    in a convenient, object-oriented way.
    """
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        Initialize the API client.
        
        Args:
            base_url (str): The base URL of the API server.
        """
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'Flaxem-Systems-API-Client/1.0'
        })
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check if the API is running and accessible.
        
        Returns:
            dict: Response from the root endpoint.
        """
        try:
            response = self.session.get(f"{self.base_url}/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Health check failed: {e}")
            return {}
    
    def get_all_posts(self) -> Dict[str, Any]:
        """
        Retrieve all blog posts from the API.
        
        Returns:
            dict: Response containing all posts.
        """
        try:
            response = self.session.get(f"{self.base_url}/posts")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to get posts: {e}")
            return {}
    
    def create_post(self, title: str, content: str, 
                   published: bool = True, rating: Optional[int] = None) -> Dict[str, Any]:
        """
        Create a new blog post.
        
        Args:
            title (str): The title of the post.
            content (str): The content of the post.
            published (bool): Whether the post is published.
            rating (Optional[int]): Optional rating for the post.
        
        Returns:
            dict: Response from the create post endpoint.
        """
        post_data = {
            "title": title,
            "content": content,
            "published": published
        }
        
        if rating is not None:
            post_data["rating"] = rating
        
        try:
            response = self.session.post(f"{self.base_url}/posts", json=post_data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to create post: {e}")
            return {}


def demonstrate_api_usage():
    """
    Demonstrate all API functionality with example data.
    
    This function shows how to use the BlogAPIClient to interact
    with all available endpoints.
    """
    print("🚀 Flaxem Systems Blog API - Usage Demonstration")
    print("=" * 50)
    
    # Initialize the API client
    client = BlogAPIClient()
    
    # 1. Health Check
    print("\n1. 🏥 Health Check")
    print("-" * 20)
    health_status = client.health_check()
    if health_status:
        print(f"✅ API is running: {json.dumps(health_status, indent=2)}")
    else:
        print("❌ API is not accessible. Make sure the server is running.")
        return
    
    # 2. Get initial posts
    print("\n2. 📖 Getting Initial Posts")
    print("-" * 30)
    initial_posts = client.get_all_posts()
    if initial_posts:
        print(f"Current posts: {json.dumps(initial_posts, indent=2)}")
    else:
        print("❌ Failed to retrieve posts")
        return
    
    # 3. Create new posts
    print("\n3. ✍️  Creating New Posts")
    print("-" * 25)
    
    # Sample posts to create
    sample_posts = [
        {
            "title": "Introduction to FastAPI",
            "content": "FastAPI is a modern, fast web framework for building APIs with Python 3.7+. It's based on standard Python type hints and provides automatic API documentation.",
            "published": True,
            "rating": 5
        },
        {
            "title": "Understanding Pydantic Models",
            "content": "Pydantic models provide data validation and serialization for Python applications. They ensure data integrity and provide excellent developer experience.",
            "published": True,
            "rating": 4
        },
        {
            "title": "Draft: Advanced API Patterns",
            "content": "This post covers advanced patterns for building robust APIs including error handling, authentication, and performance optimization.",
            "published": False,
            "rating": None
        }
    ]
    
    for i, post in enumerate(sample_posts, 1):
        print(f"\nCreating post {i}: '{post['title']}'")
        result = client.create_post(**post)
        if result:
            print(f"✅ Created: {json.dumps(result, indent=2)}")
        else:
            print(f"❌ Failed to create post {i}")
        
        # Small delay between requests
        time.sleep(0.5)
    
    # 4. Get updated posts list
    print("\n4. 📚 Getting Updated Posts List")
    print("-" * 35)
    updated_posts = client.get_all_posts()
    if updated_posts:
        posts_data = updated_posts.get('data', [])
        print(f"Total posts: {len(posts_data)}")
        print(f"Updated posts: {json.dumps(updated_posts, indent=2)}")
        
        # Show some statistics
        published_count = sum(1 for post in posts_data if post.get('published', True))
        rated_posts = [post for post in posts_data if post.get('rating') is not None]
        
        print(f"\n📊 Statistics:")
        print(f"   - Published posts: {published_count}")
        print(f"   - Draft posts: {len(posts_data) - published_count}")
        print(f"   - Rated posts: {len(rated_posts)}")
        if rated_posts:
            avg_rating = sum(post['rating'] for post in rated_posts) / len(rated_posts)
            print(f"   - Average rating: {avg_rating:.1f}")
    else:
        print("❌ Failed to retrieve updated posts")
    
    print("\n🎉 API Demonstration Complete!")
    print("\nNext steps:")
    print("- Visit http://localhost:8000/docs for interactive API documentation")
    print("- Check the API_DOCUMENTATION.md file for detailed information")
    print("- Explore the code in main.py and web.py")


def demonstrate_error_handling():
    """
    Demonstrate error handling scenarios.
    
    This function shows how the API handles various error conditions
    and how to handle them in client code.
    """
    print("\n🚨 Error Handling Demonstration")
    print("=" * 35)
    
    client = BlogAPIClient()
    
    # Test with invalid data
    print("\n1. Testing with invalid data (missing required fields)")
    try:
        response = requests.post(
            f"{client.base_url}/posts",
            json={"published": True},  # Missing title and content
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 422:
            print("✅ Validation error handled correctly:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Unexpected status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    # Test with wrong endpoint
    print("\n2. Testing with non-existent endpoint")
    try:
        response = requests.get(f"{client.base_url}/nonexistent")
        print(f"Status code: {response.status_code}")
        if response.status_code == 404:
            print("✅ 404 error handled correctly")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    """
    Main execution block.
    
    Run this script to see a complete demonstration of the API functionality.
    Make sure the FastAPI server is running before executing this script.
    """
    try:
        # Run the main demonstration
        demonstrate_api_usage()
        
        # Demonstrate error handling
        demonstrate_error_handling()
        
        print("\n" + "=" * 50)
        print("For more examples and detailed documentation:")
        print("- README.md: Project overview and quick start")
        print("- API_DOCUMENTATION.md: Comprehensive API documentation")
        print("- Interactive docs: http://localhost:8000/docs")
        
    except KeyboardInterrupt:
        print("\n\n👋 Demonstration interrupted by user")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Make sure the FastAPI server is running with: uvicorn main:app --reload")