#!/usr/bin/env python3
"""
MCP Server for JSONPlaceholder API
A free public REST API for testing and prototyping
"""

import json
import logging
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("jsonplaceholder-server")

BASE_URL = "https://jsonplaceholder.typicode.com"

mcp = FastMCP("JSONPlaceholder Server")

async def make_api_request(endpoint: str, method: str = "GET", data: dict = None) -> dict:
    """Make an HTTP request to the JSONPlaceholder API."""
    url = f"{BASE_URL}{endpoint}"
    
    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "GET":
                response = await client.get(url)
            elif method.upper() == "POST":
                response = await client.post(url, json=data)
            elif method.upper() == "PUT":
                response = await client.put(url, json=data)
            elif method.upper() == "DELETE":
                response = await client.delete(url)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"HTTP error occurred: {e}")
            raise
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise

@mcp.resource("posts://all")
async def get_all_posts() -> str:
    """Get all posts from JSONPlaceholder"""
    posts = await make_api_request("/posts")
    return json.dumps(posts, indent=2)

@mcp.resource("posts://{post_id}")
async def get_post(post_id: int) -> str:
    """Get a specific post by ID"""
    post = await make_api_request(f"/posts/{post_id}")
    return json.dumps(post, indent=2)

@mcp.resource("users://all")
async def get_all_users() -> str:
    """Get all users from JSONPlaceholder"""
    users = await make_api_request("/users")
    return json.dumps(users, indent=2)

@mcp.resource("users://{user_id}")
async def get_user(user_id: int) -> str:
    """Get a specific user by ID"""
    user = await make_api_request(f"/users/{user_id}")
    return json.dumps(user, indent=2)

@mcp.tool()
async def get_posts(post_id: int = None) -> str:
    """Retrieve all posts or a specific post by ID from JSONPlaceholder"""
    if post_id:
        endpoint = f"/posts/{post_id}"
    else:
        endpoint = "/posts"
    
    result = await make_api_request(endpoint)
    return json.dumps(result, indent=2)

@mcp.tool()
async def get_users(user_id: int = None) -> str:
    """Retrieve all users or a specific user by ID"""
    if user_id:
        endpoint = f"/users/{user_id}"
    else:
        endpoint = "/users"
    
    result = await make_api_request(endpoint)
    return json.dumps(result, indent=2)

@mcp.tool()
async def get_comments(post_id: int = None, comment_id: int = None) -> str:
    """Retrieve comments, optionally filtered by post ID or get a specific comment"""
    if comment_id:
        endpoint = f"/comments/{comment_id}"
    elif post_id:
        endpoint = f"/posts/{post_id}/comments"
    else:
        endpoint = "/comments"
    
    result = await make_api_request(endpoint)
    return json.dumps(result, indent=2)

@mcp.tool()
async def get_albums(user_id: int = None, album_id: int = None) -> str:
    """Retrieve albums, optionally filtered by user ID or get a specific album"""
    if album_id:
        endpoint = f"/albums/{album_id}"
    elif user_id:
        endpoint = f"/users/{user_id}/albums"
    else:
        endpoint = "/albums"
    
    result = await make_api_request(endpoint)
    return json.dumps(result, indent=2)

@mcp.tool()
async def get_photos(album_id: int = None, photo_id: int = None) -> str:
    """Retrieve photos, optionally filtered by album ID or get a specific photo"""
    if photo_id:
        endpoint = f"/photos/{photo_id}"
    elif album_id:
        endpoint = f"/albums/{album_id}/photos"
    else:
        endpoint = "/photos"
    
    result = await make_api_request(endpoint)
    return json.dumps(result, indent=2)

@mcp.tool()
async def get_todos(user_id: int = None, todo_id: int = None) -> str:
    """Retrieve todos, optionally filtered by user ID or get a specific todo"""
    if todo_id:
        endpoint = f"/todos/{todo_id}"
    elif user_id:
        endpoint = f"/users/{user_id}/todos"
    else:
        endpoint = "/todos"
    
    result = await make_api_request(endpoint)
    return json.dumps(result, indent=2)

@mcp.tool()
async def create_post(title: str, body: str, user_id: int) -> str:
    """Create a new post (simulated - JSONPlaceholder doesn't actually store data)"""
    post_data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    
    result = await make_api_request("/posts", method="POST", data=post_data)
    return f"Post created successfully (simulated):\n{json.dumps(result, indent=2)}"

@mcp.tool()
async def search_posts(query: str) -> str:
    """Search posts by title or body content"""
    posts = await make_api_request("/posts")
    
    matching_posts = []
    query_lower = query.lower()
    
    for post in posts:
        if (query_lower in post.get('title', '').lower() or 
            query_lower in post.get('body', '').lower()):
            matching_posts.append(post)
    
    return json.dumps(matching_posts, indent=2)

@mcp.prompt()
def analyze_post(post_id: int) -> str:
    """Generate a prompt to analyze a specific post"""
    return f"""Please analyze the post with ID {post_id} from JSONPlaceholder. 

First, retrieve the post data using the get_posts tool with post_id={post_id}.
Then provide an analysis covering:
1. Content summary
2. Writing style and tone
3. Key themes or topics
4. Potential audience
5. Engagement potential

Also retrieve the comments for this post using get_comments with post_id={post_id} and summarize the community response."""

@mcp.prompt()
def user_profile_summary(user_id: int) -> str:
    """Generate a prompt to create a comprehensive user profile summary"""
    return f"""Please create a comprehensive profile summary for user ID {user_id} from JSONPlaceholder.

Use these tools to gather data:
1. get_users with user_id={user_id} - Get user details
2. get_posts with user_id={user_id} - Get user's posts  
3. get_albums with user_id={user_id} - Get user's albums
4. get_todos with user_id={user_id} - Get user's todos

Create a summary including:
- Basic information (name, email, company, etc.)
- Activity level (number of posts, albums, todos)
- Content themes and interests based on posts
- Organization level based on todos completion
- Overall user engagement profile"""

if __name__ == "__main__":
    mcp.run() 