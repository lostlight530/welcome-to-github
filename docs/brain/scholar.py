import sys
import os
import json
import re
from datetime import datetime
from typing import Optional, List, Tuple

# Ensure we can import factory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from factory import KnowledgeFactory

class StaticScholar:
    """
    The Static Scholar (静态学者).
    Responsible for fetching external documentation and 'deepening' the knowledge of existing entities.
    Implements Graceful Degradation: Regex -> Heuristics -> Keyword extraction.
    """
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.factory = KnowledgeFactory(root_dir)

    def study_topic(self, entity_id: str, url: str):
        """
        Simulates fetching a URL and extracting deep architectural insights.
        Uses a robust extraction strategy (Simulated).
        """
        print(f"[Scholar] 正在研读 (Studying): {entity_id} from {url}...")

        # 1. Fetch Content (Simulated)
        # In real life: content = requests.get(url).text
        # Here we simulate different "content shapes" to test degradation logic.
        content_shape = self._simulate_content_retrieval(entity_id)

        # 2. Extract Insights (Graceful Degradation)
        insights = self._extract_insights_robust(content_shape)

        print(f"[Scholar] 提取到 {len(insights)} 条核心见解 (Insights extracted).")

        # 3. Ingest
        for i, (name, desc) in enumerate(insights, 1):
            pattern_id = f"arch_pattern_{entity_id}_{i}"
            try:
                # Idempotent Add (Factory checks exist check)
                self.factory.add_entity("concepts", {
                    "id": pattern_id,
                    "type": "pattern",
                    "name": name,
                    "desc": desc,
                    "tags": ["architecture", "deep-dive"],
                    "updated_at": datetime.now().isoformat()
                })

                self.factory.add_relation({
                    "src": entity_id,
                    "rel": "implements_philosophy",
                    "dst": pattern_id,
                    "context": f"Source: {url}",
                    "created_at": datetime.now().isoformat()
                })
                print(f"  - Injected: {name}")
            except Exception as e:
                print(f"  ! Error injecting {name}: {e}")

        print(f"[Scholar] {entity_id} 深度研读完成。灵魂已注入。")

    def _simulate_content_retrieval(self, entity_id: str) -> str:
        # Mock content based on ID
        if "gemma" in entity_id:
            return "## Architecture\n- Multi-Query Attention: Efficient inference.\n- XLA: TPU optimization."
        elif "mediapipe" in entity_id:
            return "Release Note: Added NPU support. Performance optimized."
        else:
            return "General documentation text with keywords like Scalability and Modular Design."

    def _extract_insights_robust(self, content: str) -> List[Tuple[str, str]]:
        """
        Tier 1: Regex Anchors (Structure)
        Tier 2: Bullet Points (Semi-Structure)
        Tier 3: Heuristic Keywords (Unstructured)
        """
        insights = []

        # Tier 1: Explicit Architecture Section
        match = re.search(r"## Architecture\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
        if match:
            print("  [Parser] Tier 1: Regex Architecture Block found.")
            block = match.group(1)
            for line in block.split('\n'):
                if line.strip().startswith('-'):
                    parts = line.strip('- ').split(':')
                    if len(parts) >= 2:
                        insights.append((parts[0].strip(), parts[1].strip()))
            if insights: return insights

        # Tier 2: Bullet Points scanning
        bullets = re.findall(r"[-*] (.*?): (.*)", content)
        if bullets:
            print("  [Parser] Tier 2: Bullet Points found.")
            for b in bullets:
                insights.append((b[0].strip(), b[1].strip()))
            if insights: return insights

        # Tier 3: Keyword Heuristics
        print("  [Parser] Tier 3: Keyword Extraction.")
        keywords = ["Scalability", "Performance", "Modular", "Security"]
        for k in keywords:
            if k in content:
                insights.append((f"{k} Focus", f"The documentation emphasizes {k}."))

        return insights

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scholar.py <entity_id> <url>")
        sys.exit(1)

    scholar = StaticScholar("docs/brain")
    scholar.study_topic(sys.argv[1], sys.argv[2])
