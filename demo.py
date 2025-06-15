#!/usr/bin/env python3
"""
Demo script showing how to interact with the JSONPlaceholder MCP Server
This demonstrates the tools and resources available.
"""

import asyncio
import json
from server import mcp, make_api_request

async def demo_tools():
    """Demonstrate the MCP tools functionality"""
    print("🔧 DEMO: MCP Tools (Actions)")
    print("=" * 50)
    
    from server import get_posts, get_users, search_posts, create_post
    
    print("\n1. Getting first 3 posts...")
    posts_data = await get_posts()
    posts = json.loads(posts_data)
    for i, post in enumerate(posts[:3]):
        print(f"   Post {post['id']}: {post['title'][:50]}...")
    
    print("\n2. Getting user details for user ID 1...")
    user_data = await get_users(user_id=1)
    user = json.loads(user_data)
    print(f"   User: {user['name']} ({user['email']})")
    print(f"   Company: {user['company']['name']}")
    
    print("\n3. Searching for posts containing 'dolor'...")
    search_results = await search_posts("dolor")
    results = json.loads(search_results)
    print(f"   Found {len(results)} posts containing 'dolor'")
    for post in results[:2]:
        print(f"   - {post['title'][:40]}...")
    
    print("\n4. Creating a new post...")
    new_post_data = await create_post(
        title="Demo Post from MCP Server",
        body="This is a demonstration post created via the MCP server!",
        user_id=1
    )
    print(f"   {new_post_data.split(':', 1)[0]}")

async def demo_resources():
    """Demonstrate the MCP resources functionality"""
    print("\n📄 DEMO: MCP Resources (Data Access)")
    print("=" * 50)
    
    from server import get_all_posts, get_post, get_all_users, get_user
    
    print("\n1. Loading all posts as a resource...")
    posts_resource = await get_all_posts()
    posts = json.loads(posts_resource)
    print(f"   Loaded {len(posts)} posts as resource data")
    
    print("\n2. Loading post ID 1 as a resource...")
    post_resource = await get_post(post_id=1)
    post = json.loads(post_resource)
    print(f"   Post Title: {post['title']}")
    print(f"   Post Body: {post['body'][:100]}...")
    
    print("\n3. Loading all users as a resource...")
    users_resource = await get_all_users()
    users = json.loads(users_resource)
    print(f"   Loaded {len(users)} users as resource data")
    user_names = [user['name'] for user in users[:5]]
    print(f"   First 5 users: {', '.join(user_names)}")

def demo_prompts():
    """Demonstrate the MCP prompts functionality"""
    print("\n📝 DEMO: MCP Prompts (Templates)")
    print("=" * 50)
    
    from server import analyze_post, user_profile_summary
    
    print("\n1. Generating post analysis prompt for post ID 1...")
    analysis_prompt = analyze_post(post_id=1)
    print(f"   Generated prompt length: {len(analysis_prompt)} characters")
    print(f"   Prompt preview: {analysis_prompt[:200]}...")
    
    print("\n2. Generating user profile prompt for user ID 1...")
    profile_prompt = user_profile_summary(user_id=1)
    print(f"   Generated prompt length: {len(profile_prompt)} characters")
    print(f"   Prompt preview: {profile_prompt[:200]}...")

async def main():
    """Run all demos"""
    print("🎉 JSONPlaceholder MCP Server Demo")
    print("=" * 50)
    print("This demo shows the three types of MCP primitives:")
    print("- Tools: Actions that can be performed")
    print("- Resources: Data that can be loaded as context")
    print("- Prompts: Templates for LLM interactions")
    
    print("\n🔗 Testing API connectivity...")
    try:
        posts = await make_api_request("/posts")
        print(f"✓ API is accessible - {len(posts)} posts available")
    except Exception as e:
        print(f"✗ API connection failed: {e}")
        return
    
    await demo_tools()
    await demo_resources()
    demo_prompts()
    
    print("\n🎯 Next Steps:")
    print("- Run 'uv run mcp dev server.py' to test with MCP Inspector")
    print("- Run 'uv run mcp install server.py' to add to Claude Desktop")
    print("- Use the server with any MCP-compatible client!")

if __name__ == "__main__":
    asyncio.run(main()) 