# JSONPlaceholder MCP Server

A Model Context Protocol (MCP) server that provides access to the JSONPlaceholder API - a free fake REST API for testing and prototyping.

## Features

This MCP server provides tools to interact with JSONPlaceholder's endpoints:

- **get_posts**: Retrieve all posts or a specific post by ID
- **get_users**: Retrieve all users or a specific user by ID  
- **get_comments**: Retrieve comments, optionally filtered by post ID
- **get_albums**: Retrieve albums, optionally filtered by user ID
- **get_photos**: Retrieve photos, optionally filtered by album ID
- **get_todos**: Retrieve todos, optionally filtered by user ID
- **create_post**: Create a new post (simulated - data isn't actually stored)

## Setup

### Prerequisites
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

1. Clone or download this project
2. The project is already configured with uv. Simply run:
```bash
uv sync
```

### Running the Server

```bash
uv run python server.py
```

Or alternatively, you can use the configured script:
```bash
uv run jsonplaceholder-mcp-server
```

### Testing (Optional)

Test the API integration:
```bash
uv run python test_server.py
```

## Usage

The server communicates via stdin/stdout using the MCP protocol. It's designed to be used with MCP-compatible clients.

### Example Tool Calls

- Get all posts: `get_posts`
- Get specific post: `get_posts` with `{"post_id": 1}`
- Get user's posts: `get_posts` with `{"user_id": 1}`
- Get comments for a post: `get_comments` with `{"post_id": 1}`
- Create a new post: `create_post` with `{"title": "My Title", "body": "Post content", "user_id": 1}`

## API Information

This server uses the JSONPlaceholder API (https://jsonplaceholder.typicode.com/), which provides:
- 100 posts
- 10 users  
- 500 comments
- 100 albums
- 5000 photos
- 200 todos

No API key is required as it's completely free and public.

## Development

The server is built using:
- Python 3.8+
- MCP SDK for Python
- httpx for async HTTP requests
- JSON for data serialization 