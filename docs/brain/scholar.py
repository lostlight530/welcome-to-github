import sys
import os
import json
from datetime import datetime
from typing import Optional

# Ensure we can import factory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from factory import KnowledgeFactory

class StaticScholar:
    """
    The Static Scholar (静态学者).
    Responsible for fetching external documentation and 'deepening' the knowledge of existing entities.
    负责获取外部文档并“加深”现有实体的知识。
    """
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.factory = KnowledgeFactory(root_dir)

    def study_topic(self, entity_id: str, url: str):
        """
        Simulates fetching a URL and extracting deep architectural insights.
        模拟获取 URL 并提取深层架构见解。
        """
        print(f"[Scholar] 正在研读 (Studying): {entity_id} from {url}...")

        if entity_id == "gemma-2b":
            insights = [
                ("Multi-Query Attention", "Uses MQA for efficient inference."),
                ("XLA Optimization", "Optimized for TPU/GPU execution via XLA."),
                ("Quantization Support", "Supports int8/int4 execution on mobile.")
            ]
        elif entity_id == "on-device-llm":
            insights = [
                ("Memory Management", "Requires careful memory management (RAM < 8GB)."),
                ("Delegate Acceleration", "Relies on delegate acceleration (NPU/DSP)."),
                ("Privacy-First", "Architecture ensures no data leaves device.")
            ]
        else:
            insights = [("General Pattern", f"Architectural pattern from {url}.")]

        print(f"[Scholar] 提取到 {len(insights)} 条核心见解 (Insights extracted).")

        # Ingest as "Deep Knowledge" Relations
        for i, (name, desc) in enumerate(insights, 1):
            pattern_id = f"arch_pattern_{entity_id}_{i}"

            # Step 1: Create the Pattern Entity First (Must exist!)
            # 第一步：先创建模式实体（必须存在！）
            try:
                self.factory.add_entity("concepts", {
                    "id": pattern_id,
                    "type": "pattern",
                    "name": name,
                    "desc": desc,
                    "tags": ["architecture", "deep-dive"],
                    "updated_at": datetime.now().isoformat()
                })
            except Exception as e:
                print(f"  ! Warning: Could not create pattern entity: {e}")

            # Step 2: Connect it
            # 第二步：连接它
            try:
                self.factory.add_relation({
                    "src": entity_id,
                    "rel": "implements_philosophy",
                    "dst": pattern_id,
                    "context": f"Source: {url}",
                    "created_at": datetime.now().isoformat()
                })
                print(f"  - Injected: {name}")
            except Exception as e:
                print(f"  ! Error creating relation: {e}")

        print(f"[Scholar] {entity_id} 深度研读完成。灵魂已注入。")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scholar.py <entity_id> <url>")
        sys.exit(1)

    scholar = StaticScholar("docs/brain")
    scholar.study_topic(sys.argv[1], sys.argv[2])
