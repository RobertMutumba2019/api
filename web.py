"""
Simple FastAPI Web Application

This module provides a basic web endpoint for the Flaxem Systems application.
It serves as a simple web interface or can be used as a secondary API endpoint.

Author: Flaxem Systems
Version: 1.0
"""

from fastapi import FastAPI

# Initialize FastAPI application instance for web interface
app = FastAPI(
    title="Flaxem Systems Web API",
    description="Simple web interface for Flaxem Systems",
    version="1.0.0"
)


@app.get("/")
async def view():
    """
    Root endpoint for the web application.
    
    This asynchronous endpoint returns a simple message identifying the
    Flaxem Systems application. It can be used as a health check or
    basic information endpoint.
    
    Returns:
        dict: A dictionary containing the system message.
        
    Example:
        GET /
        Response: {"message": "Flaxem Systems"}
        
    Note:
        This is an async function, making it suitable for handling
        concurrent requests efficiently.
    """
    return {"message": "Flaxem Systems"}