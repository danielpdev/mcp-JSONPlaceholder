# JSONPlaceholder MCP Server

A modern Model Context Protocol (MCP) server built with FastMCP that provides access to the JSONPlaceholder API - a free fake REST API for testing and prototyping.

## Features

This MCP server provides **Resources**, **Tools**, and **Prompts** for interacting with JSONPlaceholder:

### 🔧 **Tools** (Actions)
- **get_posts** - Retrieve all posts or a specific post by ID
- **get_users** - Retrieve all users or a specific user by ID  
- **get_comments** - Retrieve comments, optionally filtered by post ID
- **get_albums** - Retrieve albums, optionally filtered by user ID
- **get_photos** - Retrieve photos, optionally filtered by album ID
- **get_todos** - Retrieve todos, optionally filtered by user ID
- **create_post** - Create a new post (simulated)
- **search_posts** - Search posts by title or body content

### 📄 **Resources** (Data Access)
- **posts://all** - Get all posts as a resource
- **posts://{post_id}** - Get a specific post as a resource
- **users://all** - Get all users as a resource  
- **users://{user_id}** - Get a specific user as a resource

### 📝 **Prompts** (Templates)
- **analyze_post** - Generate analysis prompt for a specific post
- **user_profile_summary** - Create comprehensive user profile analysis


### How to add it to cursor:
```bash {
  "mcpServers": {
    "jsonplaceholder": {
      "command": "/Users/danielpopa/Projects/work/mcp-server/cursor_runner.sh",
      "args": []
    }
  }
} 
```

### Prerequisites
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

1. Clone or download this project
2. The project is already configured with uv. Simply run:
```bash
uv sync
```

### Development & Testing

**MCP Inspector** (recommended for development):
```bash
uv run mcp dev server.py
```
This opens an interactive web interface to test all tools, resources, and prompts.

**Direct server execution**:
```bash
uv run python server.py
```

**Test API connectivity**:
```bash
uv run python test_server.py
```

### Claude Desktop Integration

Install directly into Claude Desktop:
```bash
uv run mcp install server.py --name "JSONPlaceholder API"
```

### Usage Examples

Once connected to an MCP client, you can:

**Use Tools:**
- "Get all posts from JSONPlaceholder"
- "Show me user details for user ID 1"
- "Search for posts containing 'dolor'"
- "Create a new post titled 'Test' with body 'Hello World' for user 1"

**Access Resources:**
- The client can load `posts://all` to get all posts as context
- Load `users://5` to get user 5's details as background information

**Use Prompts:**
- Use the "analyze_post" prompt with post ID 1 for detailed post analysis
- Use "user_profile_summary" with user ID 2 for comprehensive user profiling

## API Information

This server uses the JSONPlaceholder API (https://jsonplaceholder.typicode.com/), which provides:
- 100 posts
- 10 users  
- 500 comments
- 100 albums
- 5000 photos
- 200 todos

No API key is required as it's completely free and public.

## Architecture

Built with **FastMCP**, this server demonstrates modern MCP patterns:
- **Decorator-based setup** - Clean, Pythonic code
- **Type hints** - Better development experience
- **Async/await** - Efficient HTTP requests
- **Resource management** - Proper data exposure to LLMs
- **Prompt templates** - Reusable interaction patterns
- **Development tools** - Built-in testing and debugging

## Development

The server uses:
- **FastMCP** - Modern MCP server framework
- **httpx** - Async HTTP client
- **Python 3.10+** - Modern Python features
- **uv** - Fast Python package management 