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
    orphan_nodes: List[str]
    stale_nodes: List[str]
    broken_links: List[str]
    density: float

class Cortex:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.entities: Dict[str, Entity] = {}
        self.relations: List[Relation] = []
        self.snapshot_path = os.path.join(root_dir, "knowledge", "snapshot.json")

    def load_graph(self):
        """
        Loads graph from snapshot first (O(1)), then merges delta .jsonl files.
        """
        # 1. Load Snapshot if exists
        loaded_snapshot_time = None
        if os.path.exists(self.snapshot_path):
            print(f"[Cortex] Loading snapshot: {self.snapshot_path}")
            try:
                with open(self.snapshot_path, 'r') as f:
                    data = json.load(f)
                    for e_data in data.get('entities', []):
                        self.entities[e_data['id']] = Entity(**e_data)
                    for r_data in data.get('relations', []):
                        self.relations.append(Relation(**r_data))
                    loaded_snapshot_time = data.get('timestamp')
                    print(f"  - Snapshot loaded ({len(self.entities)} entities, {len(self.relations)} relations).")
            except Exception as e:
                print(f"  ! Error loading snapshot: {e}")

        # 2. Load Delta (New .jsonl files)
        # In a real LSM tree, we'd only load files newer than snapshot time.
        # For simplicity/robustness, we re-scan everything but update/dedupe in memory.
        # Ideally, we should check file mtime.

        self._load_jsonl_entities()
        self._load_jsonl_relations()

    def _load_jsonl_entities(self):
        entity_path = os.path.join(self.root_dir, "knowledge", "entities", "**", "*.jsonl")
        for filepath in glob.glob(entity_path, recursive=True):
            with open(filepath, 'r') as f:
                for line in f:
                    if not line.strip(): continue
                    try:
                        data = json.loads(line)
                        if 'id' in data:
                            # Overwrite or Add (Last Write Wins)
                            self.entities[data['id']] = Entity(**data)
                    except json.JSONDecodeError:
                        pass

    def _load_jsonl_relations(self):
        rel_path = os.path.join(self.root_dir, "knowledge", "relations", "**", "*.jsonl")
        # To avoid duplicates if we loaded from snapshot, we might need logic.
        # But since relations are Append-Only logs, simple appending works if snapshot + delta = total history.
        # The issue is if snapshot *contains* data from .jsonl, loading .jsonl again duplicates relations.
        # FIX: Compact should DELETE or ARCHIVE old .jsonl files, or we track parsed files.
        # STRATEGY: Snapshot is a "Cache". We clear memory before loading delta if we want perfect sync,
        # OR we assume snapshot is the "Base" and we only load files *newer* than snapshot.
        # For this version: We will simple clear relations from memory before loading JSONL
        # IF we want to rely on JSONL as source of truth.
        # BUT the goal of snapshot is speed.
        # Let's use a simple Set for relation deduplication based on (src, rel, dst).

        existing_rels = {(r.src, r.rel, r.dst) for r in self.relations}

        for filepath in glob.glob(rel_path, recursive=True):
            with open(filepath, 'r') as f:
                for line in f:
                    if not line.strip(): continue
                    try:
                        data = json.loads(line)
                        if 'src' in data and 'dst' in data:
                            key = (data['src'], data['rel'], data['dst'])
                            if key not in existing_rels:
                                self.relations.append(Relation(**data))
                                existing_rels.add(key)
                    except json.JSONDecodeError:
                        pass

    def save_snapshot(self):
        """
        Compacts current memory state into a single JSON snapshot.
        """
        print(f"[Cortex] Creating snapshot at {self.snapshot_path}...")
        data = {
            "timestamp": datetime.now().isoformat(),
            "entities": [asdict(e) for e in self.entities.values()],
            "relations": [asdict(r) for r in self.relations]
        }
        with open(self.snapshot_path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[Cortex] Snapshot saved. Size: {len(self.entities)} entities, {len(self.relations)} relations.")

    def query_entity(self, entity_id: str) -> Optional[Dict]:
        if entity_id not in self.entities:
            return None
        entity = self.entities[entity_id]
        outgoing = [r for r in self.relations if r.src == entity_id]
        incoming = [r for r in self.relations if r.dst == entity_id]
        return {
            "node": asdict(entity),
            "connections": {
                "outgoing": [{"rel": r.rel, "target": r.dst, "context": r.context} for r in outgoing],
                "incoming": [{"rel": r.rel, "source": r.src, "context": r.context} for r in incoming]
            }
        }

    def search_concepts(self, query: str) -> List[Entity]:
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
        if start_id not in self.entities or end_id not in self.entities:
            return None
        queue = deque([(start_id, [start_id])])
        visited = {start_id}
        adj: Dict[str, List[str]] = {eid: [] for eid in self.entities}
        for rel in self.relations:
            if rel.src in adj: adj[rel.src].append(rel.dst)
            if rel.dst in adj: adj[rel.dst].append(rel.src)
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
        lines = ["graph TD"]
        types = set(e.type for e in self.entities.values())
        for t in types:
            lines.append(f"  subgraph {t.upper()}")
            for e in self.entities.values():
                if e.type == t:
                    safe_name = e.name.replace('"', '').replace('(', '').replace(')', '')
                    lines.append(f"    {e.id}(\"{safe_name}\")")
            lines.append("  end")
        for rel in self.relations:
            if rel.src in self.entities and rel.dst in self.entities:
                label = rel.rel.replace('"', '')
                lines.append(f"  {rel.src} -- \"{label}\" --> {rel.dst}")
        return "\n".join(lines)

    def validate_graph(self) -> List[str]:
        errors = []
        for i, rel in enumerate(self.relations):
            if rel.src not in self.entities:
                errors.append(f"Broken Link: Relation #{i} source '{rel.src}' does not exist.")
            if rel.dst not in self.entities:
                errors.append(f"Broken Link: Relation #{i} destination '{rel.dst}' does not exist.")
        return errors

    def analyze_entropy(self, stale_days: int = 30) -> EntropyReport:
        indegree = {eid: 0 for eid in self.entities}
        outdegree = {eid: 0 for eid in self.entities}
        for rel in self.relations:
            if rel.src in outdegree: outdegree[rel.src] += 1
            if rel.dst in indegree: indegree[rel.dst] += 1
        orphans = [eid for eid in self.entities if indegree[eid] == 0 and outdegree[eid] == 0]
        stale_threshold = datetime.now() - timedelta(days=stale_days)
        stale_nodes = []
        for eid, entity in self.entities.items():
            if not entity.updated_at:
                stale_nodes.append(eid)
                continue
            try:
                update_date = datetime.fromisoformat(entity.updated_at.replace('Z', '+00:00'))
                if update_date.tzinfo is None: update_date = update_date.replace(tzinfo=None)
                if update_date < stale_threshold: stale_nodes.append(eid)
            except ValueError:
                stale_nodes.append(eid)
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
