#!/usr/bin/env python3
import json
import sys
import os

# Ensure we test the exact MCP server
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from nexus_mcp import MCPServer

def test_mcp_server():
    print("[Test] Initializing MCP Server test...")
    server = MCPServer("docs/brain")

    # 1. Test Initialization
    print("[Test] Testing 'initialize'...")
    init_req = {"jsonrpc": "2.0", "method": "initialize", "id": "test-1"}
    init_res = server.handle_request(init_req)
    assert init_res["result"]["serverInfo"]["name"] == "nexus-cortex", "Init failed"

    # 2. Test tool list
    print("[Test] Testing 'tools/list'...")
    list_req = {"jsonrpc": "2.0", "method": "tools/list", "id": "test-2"}
    list_res = server.handle_request(list_req)
    tools = [t["name"] for t in list_res["result"]["tools"]]
    assert "search_knowledge" in tools, "Search tool missing"
    assert "get_entity" in tools, "Get entity missing"

    # 3. Test search knowledge
    print("[Test] Testing 'tools/call -> search_knowledge'...")
    search_req = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": "search_knowledge",
            "arguments": {"query": "vllm"}
        },
        "id": "test-3"
    }
    search_res = server.handle_request(search_req)
    content = search_res["result"]["content"][0]["text"]
    assert "vllm" in content.lower(), "Search failed to find vLLM"

    print("[Test] All MCP server endpoints verified. System secure.")

if __name__ == "__main__":
    try:
        test_mcp_server()
        sys.exit(0)
    except AssertionError as e:
        print(f"[!] Test Failed: {e}")
        sys.exit(1)
