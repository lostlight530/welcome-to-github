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
    weight: float = 1.0
    last_activated: str = ""

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
        Calculates dynamic decay based on last_activated.
        """
        # 1. Load Snapshot if exists
        if os.path.exists(self.snapshot_path):
            print(f"[Cortex] Loading snapshot: {self.snapshot_path}")
            try:
                with open(self.snapshot_path, 'r') as f:
                    data = json.load(f)
                    for e_data in data.get('entities', []):
                        # Handle old snapshots missing new fields
                        if 'weight' not in e_data: e_data['weight'] = 1.0
                        if 'last_activated' not in e_data: e_data['last_activated'] = e_data.get('updated_at', '')
                        self.entities[e_data['id']] = Entity(**e_data)
                    for r_data in data.get('relations', []):
                        self.relations.append(Relation(**r_data))
                    print(f"  - Snapshot loaded ({len(self.entities)} entities, {len(self.relations)} relations).")
            except Exception as e:
                print(f"  ! Error loading snapshot: {e}")

        # 2. Load Delta (New .jsonl files)
        self._load_jsonl_entities()
        self._load_jsonl_relations()

        # 3. Apply Biological Decay (In-Memory)
        self._apply_memory_decay()

        # 4. Build Search Index
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
                            if 'weight' not in data: data['weight'] = 1.0
                            if 'last_activated' not in data: data['last_activated'] = data.get('updated_at', '')
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

    def _apply_memory_decay(self):
        """Simulates biological forgetting by applying a decay factor based on time since last activation."""
        now = datetime.now()
        for eid, entity in self.entities.items():
            if not entity.last_activated:
                continue
            try:
                last_act = datetime.fromisoformat(entity.last_activated.replace('Z', '+00:00'))
                if last_act.tzinfo is None: last_act = last_act.replace(tzinfo=None)
                days_passed = (now - last_act).days
                if days_passed > 0:
                    # Decay: weight * (0.9 ^ days), floor at 0.1
                    decayed_weight = entity.weight * (0.9 ** days_passed)
                    entity.weight = max(0.1, decayed_weight)
            except ValueError:
                pass

    def _build_search_index(self):
        """Builds in-memory SQLite FTS5 index for entities."""
        self.db = sqlite3.connect(':memory:')
        c = self.db.cursor()

        # Create FTS5 virtual table. Include weight for sorting.
        try:
            c.execute('''
                CREATE VIRTUAL TABLE entities_idx USING fts5(id, name, desc, tags, weight UNINDEXED)
            ''')
        except sqlite3.OperationalError:
            print("[Cortex] FTS5 not available. Fallback to standard table (slow search).")
            c.execute('''
                CREATE TABLE entities_idx (id TEXT, name TEXT, desc TEXT, tags TEXT, weight REAL)
            ''')

        # Batch insert
        data = []
        for e in self.entities.values():
            tags_str = ",".join(e.tags)
            data.append((e.id, e.name, e.desc, tags_str, e.weight))

        c.executemany('INSERT INTO entities_idx(id, name, desc, tags, weight) VALUES (?, ?, ?, ?, ?)', data)
        self.db.commit()

    def search_concepts(self, query: str) -> List[Entity]:
        """Performs full-text search using SQLite FTS5, ranking by FTS rank AND neural weight."""
        if not self.db:
            return []

        c = self.db.cursor()
        try:
            safe_query = query.replace('"', '""')

            # Use MATCH and order by a combination of relevance and neural weight
            # FTS5 rank is usually negative (more negative = better). We want high weight to boost it.
            c.execute('''
                SELECT id
                FROM entities_idx
                WHERE entities_idx MATCH ?
                ORDER BY rank - (weight * 10)
            ''', (safe_query,))
            ids = [row[0] for row in c.fetchall()]

            results = []
            for eid in ids:
                if eid in self.entities:
                    results.append(self.entities[eid])
            return results
        except sqlite3.OperationalError as e:
            term = f"%{query}%"
            c.execute('SELECT id FROM entities_idx WHERE id LIKE ? OR name LIKE ? OR desc LIKE ? OR tags LIKE ? ORDER BY weight DESC', (term, term, term, term))
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

        now = datetime.now()

        # Calculate degrees
        degrees = {eid: indegree[eid] + outdegree[eid] for eid in self.entities}

        orphans = []
        stale_nodes = []

        fresh_days = 3

        for eid, entity in self.entities.items():
            if degrees[eid] == 0:
                orphans.append(eid)
                continue

            # Stale check: low degree OR very low neural weight
            if degrees[eid] < 3 or entity.weight < 0.3:
                is_fresh = False
                if entity.updated_at:
                    try:
                        update_date = datetime.fromisoformat(entity.updated_at.replace('Z', '+00:00'))
                        if update_date.tzinfo is None: update_date = update_date.replace(tzinfo=None)
                        if (now - update_date).days <= fresh_days:
                            is_fresh = True
                    except ValueError:
                        pass

                # If it's heavy (high weight) but low degree, we might still want to explore it?
                # Actually, if it's heavily weighted, we know about it. Stale is for forgotten things.
                if not is_fresh and entity.weight < 0.5:
                    stale_nodes.append(eid)

        # Sort stale nodes by weight (lowest first) so we fix the most forgotten links
        stale_nodes.sort(key=lambda x: self.entities[x].weight)

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
