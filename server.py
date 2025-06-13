#!/usr/bin/env python3
"""
MCP Server for JSONPlaceholder API
A free public REST API for testing and prototyping
"""

import asyncio
import json
import logging
from typing import Any, Sequence
import httpx
from mcp.server import Server
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("jsonplaceholder-server")

# Base URL for JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Initialize the MCP server
server = Server("jsonplaceholder-server")

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

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="get_posts",
            description="Retrieve all posts or a specific post by ID from JSONPlaceholder",
            inputSchema={
                "type": "object",
                "properties": {
                    "post_id": {
                        "type": "integer",
                        "description": "Optional: ID of specific post to retrieve"
                    }
                }
            }
        ),
        types.Tool(
            name="get_users",
            description="Retrieve all users or a specific user by ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "integer",
                        "description": "Optional: ID of specific user to retrieve"
                    }
                }
            }
        ),
        types.Tool(
            name="get_comments",
            description="Retrieve comments, optionally filtered by post ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "post_id": {
                        "type": "integer",
                        "description": "Optional: ID of post to get comments for"
                    },
                    "comment_id": {
                        "type": "integer",
                        "description": "Optional: ID of specific comment to retrieve"
                    }
                }
            }
        ),
        types.Tool(
            name="get_albums",
            description="Retrieve albums, optionally filtered by user ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "integer",
                        "description": "Optional: ID of user to get albums for"
                    },
                    "album_id": {
                        "type": "integer",
                        "description": "Optional: ID of specific album to retrieve"
                    }
                }
            }
        ),
        types.Tool(
            name="get_photos",
            description="Retrieve photos, optionally filtered by album ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "album_id": {
                        "type": "integer",
                        "description": "Optional: ID of album to get photos for"
                    },
                    "photo_id": {
                        "type": "integer",
                        "description": "Optional: ID of specific photo to retrieve"
                    }
                }
            }
        ),
        types.Tool(
            name="get_todos",
            description="Retrieve todos, optionally filtered by user ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "integer",
                        "description": "Optional: ID of user to get todos for"
                    },
                    "todo_id": {
                        "type": "integer",
                        "description": "Optional: ID of specific todo to retrieve"
                    }
                }
            }
        ),
        types.Tool(
            name="create_post",
            description="Create a new post (simulated - JSONPlaceholder doesn't actually store data)",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Title of the post"
                    },
                    "body": {
                        "type": "string",
                        "description": "Body content of the post"
                    },
                    "user_id": {
                        "type": "integer",
                        "description": "ID of the user creating the post"
                    }
                },
                "required": ["title", "body", "user_id"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, Any] | None
) -> list[types.TextContent]:
    """Handle tool calls."""
    if arguments is None:
        arguments = {}
    
    try:
        if name == "get_posts":
            post_id = arguments.get("post_id")
            if post_id:
                endpoint = f"/posts/{post_id}"
            else:
                endpoint = "/posts"
            
            result = await make_api_request(endpoint)
            return [
                types.TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )
            ]
        
        elif name == "get_users":
            user_id = arguments.get("user_id")
            if user_id:
                endpoint = f"/users/{user_id}"
            else:
                endpoint = "/users"
            
            result = await make_api_request(endpoint)
            return [
                types.TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )
            ]
        
        elif name == "get_comments":
            post_id = arguments.get("post_id")
            comment_id = arguments.get("comment_id")
            
            if comment_id:
                endpoint = f"/comments/{comment_id}"
            elif post_id:
                endpoint = f"/posts/{post_id}/comments"
            else:
                endpoint = "/comments"
            
            result = await make_api_request(endpoint)
            return [
                types.TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )
            ]
        
        elif name == "get_albums":
            user_id = arguments.get("user_id")
            album_id = arguments.get("album_id")
            
            if album_id:
                endpoint = f"/albums/{album_id}"
            elif user_id:
                endpoint = f"/users/{user_id}/albums"
            else:
                endpoint = "/albums"
            
            result = await make_api_request(endpoint)
            return [
                types.TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )
            ]
        
        elif name == "get_photos":
            album_id = arguments.get("album_id")
            photo_id = arguments.get("photo_id")
            
            if photo_id:
                endpoint = f"/photos/{photo_id}"
            elif album_id:
                endpoint = f"/albums/{album_id}/photos"
            else:
                endpoint = "/photos"
            
            result = await make_api_request(endpoint)
            return [
                types.TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )
            ]
        
        elif name == "get_todos":
            user_id = arguments.get("user_id")
            todo_id = arguments.get("todo_id")
            
            if todo_id:
                endpoint = f"/todos/{todo_id}"
            elif user_id:
                endpoint = f"/users/{user_id}/todos"
            else:
                endpoint = "/todos"
            
            result = await make_api_request(endpoint)
            return [
                types.TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )
            ]
        
        elif name == "create_post":
            title = arguments.get("title")
            body = arguments.get("body")
            user_id = arguments.get("user_id")
            
            if not all([title, body, user_id]):
                raise ValueError("title, body, and user_id are required for creating a post")
            
            post_data = {
                "title": title,
                "body": body,
                "userId": user_id
            }
            
            result = await make_api_request("/posts", method="POST", data=post_data)
            return [
                types.TextContent(
                    type="text",
                    text=f"Post created successfully (simulated):\n{json.dumps(result, indent=2)}"
                )
            ]
        
        else:
            raise ValueError(f"Unknown tool: {name}")
    
    except Exception as e:
        logger.error(f"Error in tool {name}: {e}")
        return [
            types.TextContent(
                type="text",
                text=f"Error: {str(e)}"
            )
        ]

async def main():
    """Run the server using stdin/stdout streams."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="jsonplaceholder-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=None,
                    experimental_capabilities=None,
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main()) 