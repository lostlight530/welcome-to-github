import json
import os
import glob
import sqlite3
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
        self.db = None # SQLite connection

    def load_graph(self):
        """
        Loads graph from snapshot first (O(1)), then merges delta .jsonl files.
        Builds SQLite FTS5 index in memory.
        """
        # 1. Load Snapshot if exists
        if os.path.exists(self.snapshot_path):
            print(f"[Cortex] Loading snapshot: {self.snapshot_path}")
            try:
                with open(self.snapshot_path, 'r') as f:
                    data = json.load(f)
                    for e_data in data.get('entities', []):
                        self.entities[e_data['id']] = Entity(**e_data)
                    for r_data in data.get('relations', []):
                        self.relations.append(Relation(**r_data))
                    print(f"  - Snapshot loaded ({len(self.entities)} entities, {len(self.relations)} relations).")
            except Exception as e:
                print(f"  ! Error loading snapshot: {e}")

        # 2. Load Delta (New .jsonl files)
        self._load_jsonl_entities()
        self._load_jsonl_relations()

        # 3. Build Search Index
        self._build_search_index()

    def _load_jsonl_entities(self):
        entity_path = os.path.join(self.root_dir, "knowledge", "entities", "**", "*.jsonl")
        for filepath in glob.glob(entity_path, recursive=True):
            with open(filepath, 'r') as f:
                for line in f:
                    if not line.strip(): continue
                    try:
                        data = json.loads(line)
                        if 'id' in data:
                            self.entities[data['id']] = Entity(**data)
                    except json.JSONDecodeError:
                        pass

    def _load_jsonl_relations(self):
        rel_path = os.path.join(self.root_dir, "knowledge", "relations", "**", "*.jsonl")
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

    def _build_search_index(self):
        """Builds in-memory SQLite FTS5 index for entities."""
        self.db = sqlite3.connect(':memory:')
        c = self.db.cursor()

        # Create FTS5 virtual table
        try:
            c.execute('''
                CREATE VIRTUAL TABLE entities_idx USING fts5(id, name, desc, tags)
            ''')
        except sqlite3.OperationalError:
            # Fallback for environments without FTS5 (though uncommon in Python 3.10+)
            print("[Cortex] FTS5 not available. Fallback to standard table (slow search).")
            c.execute('''
                CREATE TABLE entities_idx (id TEXT, name TEXT, desc TEXT, tags TEXT)
            ''')

        # Batch insert
        data = []
        for e in self.entities.values():
            tags_str = ",".join(e.tags)
            data.append((e.id, e.name, e.desc, tags_str))

        c.executemany('INSERT INTO entities_idx(id, name, desc, tags) VALUES (?, ?, ?, ?)', data)
        self.db.commit()
        print(f"[Cortex] Search index built in memory ({len(data)} records).")

    def search_concepts(self, query: str) -> List[Entity]:
        """Performs full-text search using SQLite FTS5."""
        if not self.db:
            return []

        c = self.db.cursor()
        try:
            # FTS5 match query
            # We sanitize simple queries, but let's assume basic input for now.
            # "query" -> matches any column
            # Note: FTS5 query syntax is strict. 'vllm' works. 'vllm*' works.
            # But simple words might fail if they are stopwords or syntax.
            # Let's wrap in quotes if it contains spaces to treat as phrase?
            # Or just pass raw query.

            # Simple sanitization
            safe_query = query.replace('"', '""')

            # Use MATCH
            c.execute('SELECT id FROM entities_idx WHERE entities_idx MATCH ? ORDER BY rank', (safe_query,))
            ids = [row[0] for row in c.fetchall()]

            results = []
            for eid in ids:
                if eid in self.entities:
                    results.append(self.entities[eid])
            return results
        except sqlite3.OperationalError as e:
            # Try LIKE fallback if MATCH fails (e.g. FTS not enabled or syntax error)
            # print(f"[!] Search Error (FTS): {e}. Fallback to LIKE.")
            term = f"%{query}%"
            c.execute('SELECT id FROM entities_idx WHERE id LIKE ? OR name LIKE ? OR desc LIKE ? OR tags LIKE ?', (term, term, term, term))
            ids = [row[0] for row in c.fetchall()]
            results = []
            for eid in ids:
                 if eid in self.entities:
                    results.append(self.entities[eid])
            return results

    def save_snapshot(self):
        print(f"[Cortex] Creating snapshot at {self.snapshot_path}...")
        data = {
            "timestamp": datetime.now().isoformat(),
            "entities": [asdict(e) for e in self.entities.values()],
            "relations": [asdict(r) for r in self.relations]
        }
        with open(self.snapshot_path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[Cortex] Snapshot saved. Size: {len(self.entities)} entities, {len(self.relations)} relations.")

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

    def validate_graph(self) -> List[str]:
        errors = []
        for i, rel in enumerate(self.relations):
            if rel.src not in self.entities:
                errors.append(f"Broken Link: Relation #{i} source '{rel.src}' does not exist.")
            if rel.dst not in self.entities:
                errors.append(f"Broken Link: Relation #{i} destination '{rel.dst}' does not exist.")
        return errors

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
