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
        :param category: The subdirectory/filename base (e.g., 'tech_stack', 'concepts')
        :param data: The entity data dictionary
        """
        # 1. Validate Schema (验证架构)
        try:
            entity = Entity(**data)
        except TypeError as e:
            raise ValueError(f"Invalid Entity Schema for '{data.get('id', 'unknown')}': {e}")

        # 2. Check Duplicate (检查重复)
        if entity.id in self.cortex.entities:
            print(f"[Factory] Entity '{entity.id}' already exists. Skipping. (实体已存在，跳过)")
            return

        # 3. Determine File Path (确定文件路径)
        if category.endswith('.jsonl'):
            filename = category
        else:
            filename = f"{category}.jsonl"

        filepath = os.path.join(self.root_dir, "knowledge", "entities", filename)

        # 4. Write (写入)
        self._append_line(filepath, asdict(entity))
        print(f"[Factory] Entity '{entity.id}' committed to {filename}. (实体已提交)")

        # Update local cache so subsequent relations can verify against it
        self.cortex.entities[entity.id] = entity

    def add_relation(self, data: Dict[str, Any]):
        """
        Adds a new relation to the knowledge graph.
        relations are sharded by YYYY-MM.
        向知识图谱添加新关系。关系按 YYYY-MM 分片。
        """
        # 1. Validate Schema (验证架构)
        try:
            relation = Relation(**data)
        except TypeError as e:
            raise ValueError(f"Invalid Relation Schema: {e}")

        # 2. Validate Integrity (Source and Dest must exist) (验证完整性：源和目标必须存在)
        if relation.src not in self.cortex.entities:
             raise ValueError(f"Integrity Error: Source '{relation.src}' not found. (源实体未找到)")

        if relation.dst not in self.cortex.entities:
             raise ValueError(f"Integrity Error: Destination '{relation.dst}' not found. (目标实体未找到)")

        # 3. Determine File Path (Time-based sharding) (确定文件路径：基于时间分片)
        current_ym = datetime.now().strftime("%Y-%m")
        filename = f"{current_ym}.jsonl"
        filepath = os.path.join(self.root_dir, "knowledge", "relations", filename)

        # 4. Write (写入)
        self._append_line(filepath, asdict(relation))
        print(f"[Factory] Relation '{relation.src} -> {relation.dst}' committed to {filename}. (关系已提交)")

        # Update local cache
        self.cortex.relations.append(relation)

    def _append_line(self, filepath: str, data: Dict):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
