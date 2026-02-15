import json
import os
import sys
from datetime import datetime
from dataclasses import asdict
from typing import Dict, Any

# Ensure we can import cortex
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cortex import Entity, Relation, Cortex

class KnowledgeFactory:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.cortex = Cortex(root_dir)
        # Pre-load to check for duplicates and integrity
        self.cortex.load_graph()

    def add_entity(self, category: str, data: Dict[str, Any]):
        """
        Adds a new entity to the knowledge graph.
        :param category: The subdirectory/filename base (e.g., 'tech_stack', 'concepts')
        :param data: The entity data dictionary
        """
        # 1. Validate Schema
        try:
            # Filter out unknown fields if necessary, or strict check
            # strict check:
            entity = Entity(**data)
        except TypeError as e:
            raise ValueError(f"Invalid Entity Schema for '{data.get('id', 'unknown')}': {e}")

        # 2. Check Duplicate
        if entity.id in self.cortex.entities:
            print(f"[Factory] Entity '{entity.id}' already exists. Skipping.")
            return

        # 3. Determine File Path
        # If category contains an extension, strip it. If not, add .jsonl
        if category.endswith('.jsonl'):
            filename = category
        else:
            filename = f"{category}.jsonl"

        filepath = os.path.join(self.root_dir, "knowledge", "entities", filename)

        # 4. Write
        self._append_line(filepath, asdict(entity))
        print(f"[Factory] Entity '{entity.id}' committed to {filename}.")

        # Update local cache so subsequent relations can verify against it
        self.cortex.entities[entity.id] = entity

    def add_relation(self, data: Dict[str, Any]):
        """
        Adds a new relation to the knowledge graph.
        relations are sharded by YYYY-MM.
        """
        # 1. Validate Schema
        try:
            relation = Relation(**data)
        except TypeError as e:
            raise ValueError(f"Invalid Relation Schema: {e}")

        # 2. Validate Integrity (Source and Dest must exist)
        if relation.src not in self.cortex.entities:
             raise ValueError(f"Integrity Error: Source '{relation.src}' not found in knowledge graph.")

        if relation.dst not in self.cortex.entities:
             raise ValueError(f"Integrity Error: Destination '{relation.dst}' not found in knowledge graph.")

        # 3. Determine File Path (Time-based sharding)
        current_ym = datetime.now().strftime("%Y-%m")
        filename = f"{current_ym}.jsonl"
        filepath = os.path.join(self.root_dir, "knowledge", "relations", filename)

        # 4. Write
        self._append_line(filepath, asdict(relation))
        print(f"[Factory] Relation '{relation.src} -> {relation.dst}' committed to {filename}.")

        # Update local cache
        self.cortex.relations.append(relation)

    def _append_line(self, filepath: str, data: Dict):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    # Self-Repair Mode: Add missing entities identified in previous step
    root = "docs/brain"
    if len(sys.argv) > 1:
        root = sys.argv[1]

    factory = KnowledgeFactory(root)

    # Missing: 'android'
    if 'android' not in factory.cortex.entities:
        factory.add_entity("tech_stack", {
            "id": "android",
            "type": "platform",
            "name": "Android",
            "desc": "Mobile operating system based on a modified version of the Linux kernel.",
            "tags": ["mobile", "os", "google"],
            "updated_at": datetime.now().isoformat()
        })

    # Missing: 'tool_use'
    if 'tool_use' not in factory.cortex.entities:
        factory.add_entity("concepts", {
            "id": "tool_use",
            "type": "concept",
            "name": "Tool Use",
            "desc": "The ability of an AI agent to invoke external functions or APIs.",
            "tags": ["agent", "capability"],
            "updated_at": datetime.now().isoformat()
        })

    # Verify repair
    print("\n--- Verifying Repair ---")
    errors = factory.cortex.validate_graph()
    if not errors:
        print("[OK] Graph Integrity Restored.")
    else:
        print(f"[!] Remaining Errors: {errors}")
