import json
import os
import glob
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Set, Tuple
from datetime import datetime, timedelta
from collections import deque

@dataclass
class Entity:
    id: str
    type: str
    name: str
    desc: str
    tags: List[str] = field(default_factory=list)
    updated_at: str = ""

@dataclass
class Relation:
    src: str
    rel: str
    dst: str
    context: str = ""
    created_at: str = ""

@dataclass
class EntropyReport:
    total_nodes: int
    total_edges: int
    orphan_nodes: List[str]  # Nodes with 0 connections (零连接节点)
    stale_nodes: List[str]   # Nodes not updated in X days (陈旧节点)
    broken_links: List[str]  # Relations pointing to non-existent nodes (断链)
    density: float           # Edges / (Nodes * (Nodes-1)) (密度)

class Cortex:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.entities: Dict[str, Entity] = {}
        self.relations: List[Relation] = []

    def load_graph(self):
        """
        Parses all .jsonl files in knowledge/entities and knowledge/relations.
        Builds the in-memory graph structure.
        解析 knowledge/entities 和 knowledge/relations 中的所有 .jsonl 文件。
        构建内存图谱结构。
        """
        # 1. Load Entities (加载实体)
        entity_path = os.path.join(self.root_dir, "knowledge", "entities", "**", "*.jsonl")
        for filepath in glob.glob(entity_path, recursive=True):
            with open(filepath, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    if not line.strip(): continue
                    try:
                        data = json.loads(line)
                        if 'id' in data:
                            self.entities[data['id']] = Entity(**data)
                    except json.JSONDecodeError as e:
                        print(f"    ! Error parsing {filepath}:{line_num}: {e}")
                    except TypeError as e:
                        print(f"    ! Schema mismatch {filepath}:{line_num}: {e}")

        # 2. Load Relations (加载关系)
        rel_path = os.path.join(self.root_dir, "knowledge", "relations", "**", "*.jsonl")
        for filepath in glob.glob(rel_path, recursive=True):
            with open(filepath, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    if not line.strip(): continue
                    try:
                        data = json.loads(line)
                        if 'src' in data and 'dst' in data:
                            self.relations.append(Relation(**data))
                    except json.JSONDecodeError as e:
                        print(f"    ! Error parsing {filepath}:{line_num}: {e}")
                    except TypeError as e:
                        print(f"    ! Schema mismatch {filepath}:{line_num}: {e}")

    def query_entity(self, entity_id: str) -> Optional[Dict]:
        """
        Retrieves an entity and its direct connections (both outgoing and incoming).
        获取实体及其直接连接（出站和入站）。
        """
        if entity_id not in self.entities:
            return None

        entity = self.entities[entity_id]

        outgoing = [r for r in self.relations if r.src == entity_id]
        incoming = [r for r in self.relations if r.dst == entity_id]

        result = {
            "node": asdict(entity),
            "connections": {
                "outgoing": [
                    {"rel": r.rel, "target": r.dst, "context": r.context}
                    for r in outgoing
                ],
                "incoming": [
                    {"rel": r.rel, "source": r.src, "context": r.context}
                    for r in incoming
                ]
            }
        }
        return result

    def search_concepts(self, query: str) -> List[Entity]:
        """
        Performs a case-insensitive fuzzy search on name, description, and tags.
        对名称、描述和标签执行不区分大小写的模糊搜索。
        """
        query = query.lower()
        results = []
        for entity in self.entities.values():
            match = (
                query in entity.name.lower() or
                query in entity.desc.lower() or
                any(query in t.lower() for t in entity.tags) or
                query == entity.id
            )
            if match:
                results.append(entity)
        return results

    def find_connection(self, start_id: str, end_id: str) -> Optional[List[str]]:
        """
        Uses BFS to find the shortest path of entity IDs between start and end.
        使用广度优先搜索 (BFS) 查找起点和终点之间实体 ID 的最短路径。
        """
        if start_id not in self.entities or end_id not in self.entities:
            return None

        queue = deque([(start_id, [start_id])])
        visited = {start_id}

        # Build adjacency list for faster traversal
        adj: Dict[str, List[str]] = {eid: [] for eid in self.entities}
        for rel in self.relations:
            if rel.src in adj: adj[rel.src].append(rel.dst)
            if rel.dst in adj: adj[rel.dst].append(rel.src) # Undirected for relevance (无向图用于关联性)

        while queue:
            (vertex, path) = queue.popleft()
            if vertex == end_id:
                return path

            for neighbor in adj.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def export_mermaid(self) -> str:
        """
        Generates a Mermaid Flowchart definition of the graph.
        生成图谱的 Mermaid 流程图定义。
        """
        lines = ["graph TD"]

        # Add Node Definitions
        types = set(e.type for e in self.entities.values())

        for t in types:
            lines.append(f"  subgraph {t.upper()}")
            for e in self.entities.values():
                if e.type == t:
                    safe_name = e.name.replace('"', '').replace('(', '').replace(')', '')
                    lines.append(f"    {e.id}(\"{safe_name}\")")
            lines.append("  end")

        # Add Relations
        for rel in self.relations:
            if rel.src in self.entities and rel.dst in self.entities:
                label = rel.rel.replace('"', '')
                lines.append(f"  {rel.src} -- \"{label}\" --> {rel.dst}")

        return "\n".join(lines)

    def validate_graph(self) -> List[str]:
        """
        Checks for referential integrity. Returns a list of errors.
        检查引用完整性。返回错误列表。
        """
        errors = []
        # Check if relation endpoints exist
        for i, rel in enumerate(self.relations):
            if rel.src not in self.entities:
                errors.append(f"Broken Link (断链): Relation #{i} source '{rel.src}' does not exist.")
            if rel.dst not in self.entities:
                errors.append(f"Broken Link (断链): Relation #{i} destination '{rel.dst}' does not exist.")

        return errors

    def analyze_entropy(self, stale_days: int = 30) -> EntropyReport:
        """
        Analyzes the graph for disorder, staleness, and gaps.
        分析图谱的无序性、陈旧度和缺口。
        """
        # Calculate degrees
        indegree = {eid: 0 for eid in self.entities}
        outdegree = {eid: 0 for eid in self.entities}

        for rel in self.relations:
            if rel.src in outdegree:
                outdegree[rel.src] += 1
            if rel.dst in indegree:
                indegree[rel.dst] += 1

        # Find Orphans (Degree 0)
        orphans = [
            eid for eid in self.entities
            if indegree[eid] == 0 and outdegree[eid] == 0
        ]

        # Find Stale Nodes
        stale_threshold = datetime.now() - timedelta(days=stale_days)
        stale_nodes = []
        for eid, entity in self.entities.items():
            if not entity.updated_at:
                stale_nodes.append(eid)
                continue
            try:
                update_date = datetime.fromisoformat(entity.updated_at.replace('Z', '+00:00'))
                if update_date.tzinfo is None:
                     update_date = update_date.replace(tzinfo=None)
                if update_date < stale_threshold:
                    stale_nodes.append(eid)
            except ValueError:
                stale_nodes.append(eid)

        # Calculate Density
        n = len(self.entities)
        max_edges = n * (n - 1) if n > 1 else 1
        density = len(self.relations) / max_edges if n > 1 else 0.0

        return EntropyReport(
            total_nodes=n,
            total_edges=len(self.relations),
            orphan_nodes=orphans,
            stale_nodes=stale_nodes,
            broken_links=self.validate_graph(),
            density=density
        )
