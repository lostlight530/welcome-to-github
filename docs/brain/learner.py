import json
import os
import glob
from dataclasses import dataclass, field
from typing import Dict, List, Optional

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

class KnowledgeGraph:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.entities: Dict[str, Entity] = {}
        self.relations: List[Relation] = []

    def load_graph(self):
        """
        Parses all .jsonl files in knowledge/entities and knowledge/relations.
        Builds the in-memory graph structure.
        """
        print(f"[Brain] Loading knowledge from {self.root_dir}...")

        # 1. Load Entities
        entity_path = os.path.join(self.root_dir, "knowledge", "entities", "**", "*.jsonl")
        for filepath in glob.glob(entity_path, recursive=True):
            print(f"  - Parsing entities: {filepath}")
            with open(filepath, 'r') as f:
                for line in f:
                    if not line.strip(): continue
                    try:
                        data = json.loads(line)
                        # Basic validation
                        if 'id' in data:
                            self.entities[data['id']] = Entity(**data)
                    except json.JSONDecodeError as e:
                        print(f"    ! Error parsing line: {e}")

        # 2. Load Relations
        rel_path = os.path.join(self.root_dir, "knowledge", "relations", "*.jsonl")
        for filepath in glob.glob(rel_path):
            print(f"  - Parsing relations: {filepath}")
            with open(filepath, 'r') as f:
                for line in f:
                    if not line.strip(): continue
                    try:
                        data = json.loads(line)
                        if 'src' in data and 'dst' in data:
                            self.relations.append(Relation(**data))
                    except json.JSONDecodeError as e:
                        print(f"    ! Error parsing line: {e}")

        print(f"[Brain] Loaded {len(self.entities)} entities and {len(self.relations)} relations.")

    def query_entity(self, entity_id: str) -> Optional[Dict]:
        """
        Retrieves an entity and its direct connections (both outgoing and incoming).
        Returns a structured dictionary or None if not found.
        """
        if entity_id not in self.entities:
            print(f"[Brain] Entity '{entity_id}' not found.")
            return None

        entity = self.entities[entity_id]

        # Find related edges
        outgoing = [r for r in self.relations if r.src == entity_id]
        incoming = [r for r in self.relations if r.dst == entity_id]

        result = {
            "node": entity.__dict__,
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

# Example Usage
if __name__ == "__main__":
    brain = KnowledgeGraph("docs/brain")
    brain.load_graph()

    # Query 'mcp'
    result = brain.query_entity("mcp")
    if result:
        print("\n--- Query Result: MCP ---")
        print(json.dumps(result, indent=2, ensure_ascii=False))
