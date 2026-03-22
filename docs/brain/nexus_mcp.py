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
from harvester import Harvester

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
                        },
                        {
                            "name": "trigger_harvester",
                            "description": "Force the system to run the Intent-Driven Whitelist Harvester probe for official sources.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "intent": {"type": "string", "description": "The specific data fetching intent. Defaults to 'fetch_release'."}
                                },
                                "required": []
                            }
                        },
                        {
                            "name": "blueprint_pipeline",
                            "description": "Phase IV Stateless Blueprint Routing: Execute a deterministic chain of tools sequentially without state.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "pipeline": {
                                        "type": "array",
                                        "items": {"type": "string"},
                                        "description": "A list of tool names to execute sequentially (e.g., ['trigger_harvester', 'search_knowledge'])"
                                    },
                                    "pipeline_args": {
                                        "type": "object",
                                        "description": "Arguments to pass through the pipeline"
                                    }
                                },
                                "required": ["pipeline"]
                            }
                        }
                    ]
                }
            }

        if method == "tools/call":
            name = params.get("name")
            args = params.get("arguments", {})

            try:
                if name == "blueprint_pipeline":
                    pipeline = args.get("pipeline", [])
                    p_args = args.get("pipeline_args", {})
                    results = []

                    # Deterministic Gate: validate agentic requests before execution
                    for tool in pipeline:
                        if tool not in ["trigger_harvester", "search_knowledge"]:
                            raise ValueError(f"Agentic Pipeline Failure: Tool '{tool}' is not a valid deterministic node.")

                        # Simulate routing execution
                        if tool == "trigger_harvester":
                            h = Harvester(self.root_dir)
                            res = h.fetch_github_data()
                            results.append({"tool": tool, "status": "Success", "fetched": len(res)})
                        elif tool == "search_knowledge":
                            q = p_args.get("query", "architecture")
                            results.append({"tool": tool, "status": "Success", "results": len(self.cortex.search(q))})

                    return {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps({"blueprint_status": "Complete", "stages": results}, ensure_ascii=False)}]
                        }
                    }

                elif name == "search_knowledge":
                    query = args.get("query")
                    # Liquid Graph Context: Augment search with immediate topological neighborhood
                    results = self.cortex.search(query)

                    liquid_context = {"search_results": results, "topological_context": []}
                    if results:
                        top_entity_id = results[0].get("id")
                        # Fetch 1-hop dependencies
                        try:
                            edges = self.cortex.conn.execute(
                                "SELECT relation, target FROM relations WHERE source = ? LIMIT 10",
                                (top_entity_id,)
                            ).fetchall()
                            liquid_context["topological_context"] = [{"relation": r[0], "target": r[1]} for r in edges]
                        except Exception as e:
                            logger.error(f"Topological extraction error: {e}")

                    return {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(liquid_context, ensure_ascii=False)}]
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
                elif name == "trigger_harvester":
                    harvester = Harvester(self.root_dir)
                    new_files = harvester.fetch_github_data()
                    msg = "Intent-driven harvest complete. No new high-signal data."
                    if new_files:
                        msg = f"Harvest complete. Fetched {len(new_files)} new context chunks into docs/brain/inputs/."
                    return {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": msg}]
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
