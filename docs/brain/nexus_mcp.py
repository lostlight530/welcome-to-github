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
from factory import KnowledgeFactory

# Basic MCP Server implementation for Stdio (Zero-Dependency)
# 实现基础的 MCP 服务器 (Stdio)

# Configure logging to stderr to not interfere with JSON-RPC on stdout
logging.basicConfig(level=logging.ERROR, stream=sys.stderr)
logger = logging.getLogger("nexus-mcp")

class MCPServer:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.cortex = Cortex(root_dir)
        self.factory = KnowledgeFactory(root_dir)
        self.cortex.load_graph() # Pre-load

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
                        "name": "nexus-cortex",
                        "version": "1.0.0"
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
                            "description": "Search the knowledge graph for concepts using full-text search.",
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
                                    "desc": {"type": "string"},
                                    "tags": {"type": "string", "description": "Comma-separated tags"}
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
                    results = self.cortex.search_concepts(query)

                    # Neural Autonomic Function: Activate memories that are searched
                    for r in results:
                        try:
                            self.factory.activate_memory(r.id)
                        except:
                            pass

                    return {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps([{"id": r.id, "name": r.name, "desc": r.desc, "weight": r.weight} for r in results], ensure_ascii=False)}]
                        }
                    }
                elif name == "get_entity":
                    eid = args.get("id")
                    if eid in self.cortex.entities:
                        e = self.cortex.entities[eid]
                        # Activate memory on read
                        try:
                            self.factory.activate_memory(eid)
                        except:
                            pass
                        return {
                            "jsonrpc": "2.0",
                            "id": msg_id,
                            "result": {
                                "content": [{"type": "text", "text": json.dumps({"id": e.id, "name": e.name, "desc": e.desc, "tags": e.tags, "weight": e.weight}, ensure_ascii=False)}]
                            }
                        }
                    else:
                        # Return empty list or specific error message? MCP spec suggests error for failure?
                        # Or just empty content. Let's return error for clarity.
                        return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32602, "message": f"Entity '{eid}' not found"}}

                elif name == "add_memory":
                    tags_str = args.get("tags", "")
                    tags = [t.strip() for t in tags_str.split(",")] if tags_str else []

                    entity_type = args.get("type", "concept")

                    # Dynamically route to correct jsonl file based on type pluralization
                    category_mapping = {
                        "tech": "tech",
                        "concept": "concepts",
                        "person": "people",
                        "project": "projects",
                        "model": "models",
                        "hardware": "hardware",
                        "tool": "tools",
                        "pattern": "patterns",
                        "standard": "standards"
                    }
                    category = category_mapping.get(entity_type, entity_type + "s")

                    self.factory.add_entity(category, {
                        "id": args.get("id"),
                        "type": entity_type,
                        "name": args.get("name"),
                        "desc": args.get("desc"),
                        "tags": tags,
                        "updated_at": datetime.now().isoformat(),
                        "weight": 1.0,
                        "last_activated": datetime.now().isoformat()
                    })
                    return {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": f"Entity '{args.get('id')}' added successfully to category '{category}'."}]
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
