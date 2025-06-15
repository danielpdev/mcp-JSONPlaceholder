#!/usr/bin/env python3
"""
Simple test script to verify the JSONPlaceholder API integration works.
"""

import asyncio
import httpx

BASE_URL = "https://jsonplaceholder.typicode.com"

async def test_api_endpoints():
    """Test basic API endpoints to ensure they're working."""
    
    async with httpx.AsyncClient() as client:
        print("Testing /posts endpoint...")
        response = await client.get(f"{BASE_URL}/posts")
        posts = response.json()
        print(f"✓ Retrieved {len(posts)} posts")
        
        print("\nTesting /posts/1 endpoint...")
        response = await client.get(f"{BASE_URL}/posts/1")
        post = response.json()
        print(f"✓ Retrieved post: {post['title']}")
        
        print("\nTesting /users endpoint...")
        response = await client.get(f"{BASE_URL}/users")
        users = response.json()
        print(f"✓ Retrieved {len(users)} users")
        
        print("\nTesting POST /posts endpoint...")
        post_data = {
            "title": "Test Post",
            "body": "This is a test post",
            "userId": 1
        }
        response = await client.post(f"{BASE_URL}/posts", json=post_data)
        new_post = response.json()
        print(f"✓ Created post with ID: {new_post['id']}")
        
        print("\n🎉 All API endpoints are working correctly!")

if __name__ == "__main__":
    asyncio.run(test_api_endpoints()) 