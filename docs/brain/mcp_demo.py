import sys
import os
import json
import re
from dataclasses import asdict
from typing import List, Optional
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from mcp.server.fastmcp import FastMCP

# Ensure we can import existing brain modules
brain_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(brain_root)

from cortex import Cortex
from factory import KnowledgeFactory

# Initialize FastMCP Server
mcp = FastMCP("Nexus Cortex Demo")

# Initialize Cortex (Read) and Factory (Write)
cortex = Cortex(brain_root)
factory = KnowledgeFactory(brain_root)

# Security Constants
ID_PATTERN = re.compile(r'^[a-z0-9-]+$')
ALLOWED_CATEGORIES = {"concepts", "tech_stack", "people", "projects"}

def validate_id(entity_id: str):
    """
    Enforces strict ID format to prevent path traversal.
    强制执行严格的 ID 格式以防止路径遍历。
    """
    if not ID_PATTERN.match(entity_id):
        raise ValueError(f"Security Violation: ID '{entity_id}' contains invalid characters. Only lowercase alphanumeric and hyphens allowed.")

def validate_category(category: str):
    """
    Enforces category whitelist to prevent arbitrary file writes.
    强制执行类别白名单以防止任意文件写入。
    """
    if category not in ALLOWED_CATEGORIES:
        raise ValueError(f"Security Violation: Category '{category}' is not allowed. Must be one of {ALLOWED_CATEGORIES}.")

@mcp.resource("knowledge://stats/entropy")
def get_entropy_stats() -> str:
    """
    Returns the current entropy report of the knowledge graph.
    返回知识图谱的当前熵值报告。
    """
    cortex.load_graph()
    report = cortex.analyze_entropy()
    return json.dumps(asdict(report), ensure_ascii=False)

@mcp.tool()
def get_entropy_report() -> str:
    """
    Triggers an immediate analysis of the knowledge graph.
    触发对知识图谱的即时分析。
    """
    return get_entropy_stats()

@mcp.tool()
def get_current_time(timezone_name: str = "UTC") -> str:
    """
    Returns the current time in the specified timezone (default: UTC).
    Format: ISO 8601 (YYYY-MM-DDTHH:MM:SS.mmmmmm+HH:MM).
    返回指定时区的当前时间（默认为 UTC）。格式：ISO 8601。
    """
    try:
        tz = ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError:
        return f"Error: Timezone '{timezone_name}' not found. Please provide a valid IANA timezone name (e.g., 'UTC', 'Asia/Shanghai', 'America/New_York')."
    except Exception as e:
        return f"Error: Invalid timezone '{timezone_name}'. {str(e)}"

    now = datetime.now(tz)
    return now.isoformat()

@mcp.tool()
def add_entity(category: str, id: str, type: str, name: str, desc: str, tags: Optional[List[str]] = None) -> str:
    """
    Safely adds a new entity to the knowledge graph.
    Strictly Append-Only: Fails if ID already exists.
    安全地向知识图谱添加新实体。严格只追加：如果 ID 已存在则失败。
    """
    # 1. Security Check: Input Sanitization (安全检查：输入清洗)
    validate_id(id)
    validate_category(category)

    # 2. Security Check: Append-Only (安全检查：只追加)
    # Reload graph to ensure we have the latest state
    cortex.load_graph()
    if id in cortex.entities:
        raise ValueError(f"Integrity Violation: Entity '{id}' already exists. Modification is forbidden.")

    # 3. Execution (执行)
    data = {
        "id": id,
        "type": type,
        "name": name,
        "desc": desc,
        "tags": tags or [],
        "updated_at": datetime.now().isoformat()
    }

    try:
        factory.add_entity(category, data)
        return f"Successfully added entity '{id}' to category '{category}'."
    except Exception as e:
        return f"Error adding entity: {str(e)}"

@mcp.tool()
def connect_entities(src: str, rel: str, dst: str, context: str = "") -> str:
    """
    Connects two existing entities.
    Fails if either entity does not exist.
    连接两个现有实体。如果任一实体不存在则失败。
    """
    # 1. Security Check: Input Sanitization (Safe-guard against injection, though less critical for relation lookup)
    validate_id(src)
    validate_id(dst)

    # 2. Security Check: Referential Integrity (安全检查：引用完整性)
    cortex.load_graph()
    if src not in cortex.entities:
        raise ValueError(f"Integrity Violation: Source entity '{src}' does not exist.")
    if dst not in cortex.entities:
        raise ValueError(f"Integrity Violation: Destination entity '{dst}' does not exist.")

    # 3. Execution (执行)
    data = {
        "src": src,
        "rel": rel,
        "dst": dst,
        "context": context,
        "created_at": None # Factory handles this? factory.add_relation calls Relation(**data).
        # Relation has created_at default "".
    }
    data["created_at"] = datetime.now().isoformat()

    try:
        factory.add_relation(data)
        return f"Successfully connected '{src}' --[{rel}]--> '{dst}'."
    except Exception as e:
        return f"Error connecting entities: {str(e)}"

if __name__ == "__main__":
    print(f"[Nexus] Starting MCP Demo Server (Full Matrix) on stdio...", file=sys.stderr)
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        print(f"[Nexus] Error: {e}", file=sys.stderr)
