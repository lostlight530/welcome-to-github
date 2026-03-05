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
        # 预加载以检查重复和完整性
        self.cortex.load_graph()

    def add_entity(self, category: str, data: Dict[str, Any]):
        """
        Adds a new entity to the knowledge graph.
        向知识图谱添加新实体。
        """
        try:
            # Ensure new fields exist for schema validation
            if 'weight' not in data: data['weight'] = 1.0
            if 'last_activated' not in data: data['last_activated'] = datetime.now().isoformat()

            entity = Entity(**data)
        except TypeError as e:
            raise ValueError(f"Invalid Entity Schema for '{data.get('id', 'unknown')}': {e}")

        if entity.id in self.cortex.entities:
            print(f"[Factory] Entity '{entity.id}' already exists. Skipping. (实体已存在，跳过)")
            return

        if category.endswith('.jsonl'):
            filename = category
        else:
            filename = f"{category}.jsonl"

        filepath = os.path.join(self.root_dir, "knowledge", "entities", filename)

        self._append_line(filepath, asdict(entity))
        print(f"[Factory] Entity '{entity.id}' committed to {filename}. (实体已提交)")

        self.cortex.entities[entity.id] = entity

    def touch_entity(self, entity_id: str):
        """Legacy touch. Now routes to activate_memory."""
        self.activate_memory(entity_id)

    def activate_memory(self, entity_id: str):
        """
        Neural Upgrade: Activates a memory, increasing its weight and updating the timestamp.
        神经升级：激活记忆，增加权重并更新时间戳。
        """
        if entity_id not in self.cortex.entities:
            raise ValueError(f"Entity '{entity_id}' not found.")

        entity = self.cortex.entities[entity_id]

        # Neural Reinforcement
        entity.weight += 0.5
        now = datetime.now().isoformat()
        entity.updated_at = now
        entity.last_activated = now

        filename = f"{entity.type}s.jsonl" # Pluralize type for file routing
        filepath = os.path.join(self.root_dir, "knowledge", "entities", filename)

        self._append_line(filepath, asdict(entity))
        print(f"[Factory] Memory '{entity.id}' activated (Weight: {entity.weight:.1f}). (记忆突触已强化)")

    def add_relation(self, data: Dict[str, Any]):
        """
        Adds a new relation to the knowledge graph.
        """
        try:
            relation = Relation(**data)
        except TypeError as e:
            raise ValueError(f"Invalid Relation Schema: {e}")

        if relation.src not in self.cortex.entities:
             raise ValueError(f"Integrity Error: Source '{relation.src}' not found.")

        if relation.dst not in self.cortex.entities:
             raise ValueError(f"Integrity Error: Destination '{relation.dst}' not found.")

        current_ym = datetime.now().strftime("%Y-%m")
        filename = f"{current_ym}.jsonl"
        filepath = os.path.join(self.root_dir, "knowledge", "relations", filename)

        self._append_line(filepath, asdict(relation))
        print(f"[Factory] Relation '{relation.src} -> {relation.dst}' committed to {filename}.")

        # Cross-activate entities upon connection
        self.activate_memory(relation.src)
        self.activate_memory(relation.dst)

        self.cortex.relations.append(relation)

    def _append_line(self, filepath: str, data: Dict):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
