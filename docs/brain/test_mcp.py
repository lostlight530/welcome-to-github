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

    # 5. Test Phase V Trust Gateway (Penalty Mechanism)
    print("[Test] Testing 'tools/call' Phase V Trust Gateway...")

    import random
    agent_id = f"test_hallucinator_{random.randint(1000, 9999)}"

    trust_req = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": "add_memory",
            "arguments": {
                "agent_id": agent_id,
                # Missing required 'id' and 'name' fields to trigger KeyError
                "desc": "This is a hallucinated entry"
            }
        },
        "id": "test-5"
    }

    # 5.1 First attempt - Should fail and slash trust
    trust_res = server.handle_request(trust_req)
    assert "error" in trust_res, "Phase V Penalty failed: Request without required fields was not rejected."
    assert "Trust slashed (-10)" in trust_res["error"]["message"], "Phase V Penalty failed: Did not slash trust appropriately."

    # 5.2 Drain Trust to 0
    print("[Test] Draining agent trust to verify physical TCP block simulation...")
    for _ in range(10): # 10 * 10 = 100 points
        server.handle_request(trust_req)

    # 5.3 Attempt after trust depleted - Should get PermissionError message
    final_res = server.handle_request(trust_req)
    assert "error" in final_res, "Phase V Block failed: Agent with depleted trust was not rejected."
    assert "Trust slashed" not in final_res["error"]["message"], "Phase V Block failed: Agent should be blocked before reaching the logic."
    assert "Dictator Rejection" in final_res["error"]["message"], f"Phase V Block failed: Did not receive PermissionError. Got: {final_res['error']['message']}"

    print("[Test] All MCP server endpoints verified. System secure. Trust Gateway Active.")

if __name__ == "__main__":
    try:
        test_mcp_server()
        sys.exit(0)
    except AssertionError as e:
        print(f"[!] Test Failed: {e}")
        sys.exit(1)
