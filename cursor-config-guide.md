# Cursor MCP Configuration Troubleshooting

## 🚨 **Red Status with 0 Tools - Solutions**

### **Solution 1: Use the MCP CLI Command (Recommended)**

Instead of using the raw Python command, use the MCP CLI which Cursor expects:

```json
{
  "mcpServers": {
    "jsonplaceholder": {
      "command": "uv",
      "args": ["run", "mcp", "run", "server.py"],
      "cwd": "/Users/danielpopa/Projects/work/mcp-server"
    }
  }
}
```

### **Solution 2: Use Node/NPX Format (Alternative)**

Since many MCP servers use Node.js, try this format:

```json
{
  "mcpServers": {
    "jsonplaceholder": {
      "command": "node",
      "args": ["-e", "require('child_process').spawn('uv', ['run', 'python', 'server.py'], {stdio: 'inherit', cwd: '/Users/danielpopa/Projects/work/mcp-server'})"],
      "cwd": "/Users/danielpopa/Projects/work/mcp-server"
    }
  }
}
```

### **Solution 3: Direct Python with Absolute Path**

```json
{
  "mcpServers": {
    "jsonplaceholder": {
      "command": "/Users/danielpopa/.local/share/uv/python/cpython-3.12.10-macos-aarch64-none/bin/python",
      "args": ["/Users/danielpopa/Projects/work/mcp-server/server.py"],
      "cwd": "/Users/danielpopa/Projects/work/mcp-server"
    }
  }
}
```

### **Solution 4: Shell Script Wrapper (Most Reliable)**

Create a shell script to handle the execution:

1. Create `run_for_cursor.sh` in your project
2. Make it executable 
3. Use it in Cursor config

### **Debugging Steps:**

1. **Check Cursor Logs**: Settings > Developer > Open Logs Directory
2. **Test Server Manually**: Run `uv run mcp run server.py` in terminal
3. **Verify Path**: Ensure all paths are absolute and correct
4. **Check Permissions**: Make sure Cursor can execute the command

### **Common Issues:**

- ❌ **Relative paths** - Use absolute paths
- ❌ **Missing `cwd`** - Always specify working directory  
- ❌ **Wrong command format** - Use the exact command that works in terminal
- ❌ **Python environment** - Cursor might not see your UV environment 