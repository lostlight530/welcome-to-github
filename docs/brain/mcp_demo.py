import sys
import os
import json
from dataclasses import asdict
from mcp.server.fastmcp import FastMCP

# Ensure we can import existing brain modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cortex import Cortex

# Initialize FastMCP Server
mcp = FastMCP("Nexus Cortex Demo")

# Initialize Cortex (Read-Only)
# We assume the script is run from repo root or docs/brain, so we need to find the root properly.
brain_root = os.path.dirname(os.path.abspath(__file__))
cortex = Cortex(brain_root)

@mcp.resource("knowledge://stats/entropy")
def get_entropy_stats() -> str:
    """
    Returns the current entropy report of the knowledge graph.
    返回知识图谱的当前熵值报告。
    """
    cortex.load_graph()
    report = cortex.analyze_entropy()

    # Convert dataclass to dict via asdict
    return json.dumps(asdict(report), ensure_ascii=False)

@mcp.tool()
def get_entropy_report() -> str:
    """
    Triggers an immediate analysis of the knowledge graph.
    触发对知识图谱的即时分析。
    """
    return get_entropy_stats()

if __name__ == "__main__":
    # Use stdio transport by default if not specified by mcp run
    print(f"[Nexus] Starting MCP Demo Server on stdio... (Brain Root: {brain_root})", file=sys.stderr)
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        print(f"[Nexus] Error: {e}", file=sys.stderr)
