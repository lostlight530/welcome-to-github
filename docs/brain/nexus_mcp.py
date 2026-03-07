#!/usr/bin/env python3
import sys
import os
import json
import logging
from datetime import datetime

# Add brain root to path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

from cortex import Cortex

# Basic MCP Server implementation for Stdio (Zero-Dependency)
# Configure logging to stderr to not interfere with JSON-RPC on stdout
logging.basicConfig(level=logging.ERROR, stream=sys.stderr)
logger = logging.getLogger("nexus-mcp")

class MCPServer:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.cortex = Cortex(os.path.join(root_dir, "cortex.db"))

    def handle_request(self, request: dict) -> dict:
        """Handles JSON-RPC 2.0 requests."""
        method = request.get("method")
        params = request.get("params", {})
        msg_id = request.get("id")

        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "nexus-cortex-mcp",
                        "version": "latest"
                    }
                }
            }

        if method == "tools/list":
             return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "search_knowledge",
                            "description": "Search the stateful knowledge graph using Synaptic Associative Search.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "query": {"type": "string", "description": "Search term"}
                                },
                                "required": ["query"]
                            }
                        },
                        {
                            "name": "get_entity",
                            "description": "Retrieve detailed information about a specific entity.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "string", "description": "Entity ID (slug)"}
                                },
                                "required": ["id"]
                            }
                        },
                        {
                            "name": "add_memory",
                            "description": "Add a new concept/entity to the knowledge base.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "string"},
                                    "name": {"type": "string"},
                                    "type": {"type": "string", "enum": ["tech", "concept", "person", "project", "model", "hardware", "tool", "pattern", "standard"]},
                                    "desc": {"type": "string"}
                                },
                                "required": ["id", "name", "type", "desc"]
                            }
                        }
                    ]
                }
            }

        if method == "tools/call":
            name = params.get("name")
            args = params.get("arguments", {})

            try:
                if name == "search_knowledge":
                    query = args.get("query")
                    results = self.cortex.search(query)
                    return {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(results, ensure_ascii=False)}]
                        }
                    }
                elif name == "get_entity":
                    eid = args.get("id")
                    entity = self.cortex.get_entity(eid)
                    if entity:
                        return {
                            "jsonrpc": "2.0",
                            "id": msg_id,
                            "result": {
                                "content": [{"type": "text", "text": json.dumps(entity, ensure_ascii=False)}]
                            }
                        }
                    else:
                        return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32602, "message": f"Entity '{eid}' not found"}}

                elif name == "add_memory":
                    self.cortex.add_entity(
                        id=args.get("id"),
                        type_slug=args.get("type", "concept"),
                        name=args.get("name"),
                        desc=args.get("desc")
                    )
                    return {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": f"Entity '{args.get('id')}' added successfully to cortex DB."}]
                        }
                    }
                else:
                    return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}
            except Exception as e:
                return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32000, "message": str(e)}}

        return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}

    def run(self):
        """Main loop reading from Stdin."""
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                request = json.loads(line)
                response = self.handle_request(request)
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()
            except json.JSONDecodeError:
                continue
            except Exception as e:
                logger.error(f"Error: {e}")
                break

if __name__ == "__main__":
    server = MCPServer(ROOT_DIR)
    server.run()
