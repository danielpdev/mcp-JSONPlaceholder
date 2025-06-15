# Global Cursor MCP Setup

## Step 1: Create Global MCP Configuration

1. Open Cursor IDE
2. Go to **Settings > MCP** 
3. Click **"Add new global MCP server"**

This will open `~/.cursor/mcp.json` file automatically.

## Step 2: Add Your Server Configuration

Add this configuration to the `~/.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "jsonplaceholder": {
      "command": "uv",
      "args": ["run", "python", "/Users/danielpopa/Projects/work/mcp-server/server.py"],
      "cwd": "/Users/danielpopa/Projects/work/mcp-server"
    }
  }
}
```

**Your exact configuration with the current project path is shown above.**

## Step 3: Refresh MCP Servers

1. Go back to **Settings > MCP** in Cursor
2. Click the **refresh button**
3. Your JSONPlaceholder server should appear in the list

## Step 4: Test the Integration

1. Open Cursor Composer (Agent mode)
2. Try commands like:
   - "Get all posts from JSONPlaceholder"
   - "Show me user details for user ID 1"
   - "Search posts containing 'dolor'"
   - "Create a new post with title 'Test' and body 'Hello from Cursor'" 