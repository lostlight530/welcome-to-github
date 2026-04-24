import json
import os
import sys
from datetime import datetime
from dataclasses import asdict
from typing import Dict, Any

# Ensure we can import cortex
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cortex import Cortex

class KnowledgeFactory:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.cortex = Cortex(os.path.join(root_dir, "cortex.db"))

    def add_entity(self, category: str, data: Dict[str, Any]):
        """
        Adds a new entity to the knowledge graph.
        向知识图谱添加新实体。
        """
        try:
            # Route to Cortex's add_entity method directly
            # data has id, type, name, desc
            _id = data.get('id')
            _type = data.get('type')
            _name = data.get('name')
            _desc = data.get('desc')

            if not all([_id, _type, _name, _desc]):
                raise ValueError(f"Invalid Entity Schema. Missing required fields in '{data}'.")

            self.cortex.add_entity(_id, _type, _name, _desc, save_to_disk=True)
            print(f"[Factory] Entity '{_id}' committed. (实体已提交)")

        except Exception as e:
            print(f"[Factory Error] Failed to add entity: {e}")

    def touch_entity(self, entity_id: str):
        """Legacy touch. Now routes to activate_memory."""
        self.activate_memory(entity_id)

    def activate_memory(self, entity_id: str):
        """
        Neural Upgrade: Activates a memory, increasing its weight and updating the timestamp.
        神经升级：激活记忆，增加权重并更新时间戳。
        """
        try:
            self.cortex.activate_memory(entity_id)
        except Exception as e:
            print(f"[Factory Error] Failed to activate memory: {e}")

    def add_relation(self, data: Dict[str, Any]):
        """
        Adds a new relation to the knowledge graph.
        """
        try:
            _src = data.get('src')
            _rel = data.get('rel')
            _dst = data.get('dst')
            _desc = data.get('context', "")

            if not all([_src, _rel, _dst]):
                raise ValueError(f"Invalid Relation Schema. Missing required fields in '{data}'.")

            self.cortex.connect_entities(_src, _rel, _dst, _desc, save_to_disk=True)
            print(f"[Factory] Relation '{_src} -> {_dst}' committed.")

        except Exception as e:
            print(f"[Factory Error] Failed to add relation: {e}")

    def _append_line(self, filepath: str, data: Dict):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "a", encoding="utf-8") as f:
                f.write(json.dumps(data, ensure_ascii=False) + "\\n")
        except Exception as e:
            print(f"[Factory Error] Failed to append to {filepath}: {e}")
