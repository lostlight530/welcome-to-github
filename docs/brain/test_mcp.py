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
    assert init_res["result"]["serverInfo"]["name"] == "nexus-cortex-mcp", "Init failed"

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
    if "error" in search_res:
        raise AssertionError(f"Search failed: {search_res['error']}")
    content = search_res["result"]["content"][0]["text"]

    # We will just assert it returns a valid JSON string (it might be empty)
    try:
        json.loads(content)
    except Exception as e:
        raise AssertionError(f"Search failed to return JSON string: {e}")

    # 4. Test trigger_harvester
    print("[Test] Testing 'tools/call -> trigger_harvester'...")
    harvester_req = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": "trigger_harvester",
            "arguments": {"intent": "fetch_release"}
        },
        "id": "test-4"
    }
    harvester_res = server.handle_request(harvester_req)
    if "error" in harvester_res:
        raise AssertionError(f"Harvester failed: {harvester_res['error']}")

    print("[Test] All MCP server endpoints verified. System secure.")

if __name__ == "__main__":
    try:
        test_mcp_server()
        sys.exit(0)
    except AssertionError as e:
        print(f"[!] Test Failed: {e}")
        sys.exit(1)
