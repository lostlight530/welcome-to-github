import sys
import os
import shutil
from datetime import datetime
from typing import List, Optional

# Ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cortex import Cortex
from factory import KnowledgeFactory

class Evolver:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.cortex = Cortex(root_dir)
        self.factory = KnowledgeFactory(root_dir)

        self.memories_dir = os.path.join(root_dir, "memories")
        self.archive_dir = os.path.join(self.memories_dir, "archive")
        self.active_mission_path = os.path.join(self.memories_dir, "MISSION_ACTIVE.md")

        os.makedirs(self.archive_dir, exist_ok=True)

    def run_cycle(self):
        """
        The main OODA loop.
        OODA 循环：观察、调整、决策、行动。
        """
        print("[Evolution] Starting Cognitive Cycle... (开始认知循环)")

        # 1. Observe (观察)
        self.cortex.load_graph()
        report = self.cortex.analyze_entropy()

        print(f"[Entropy] Density (密度): {report.density:.4f} | Orphans (孤岛): {len(report.orphan_nodes)} | Stale (陈旧): {len(report.stale_nodes)}")

        # 2. Orient (调整)
        if os.path.exists(self.active_mission_path):
            print("[Evolution] Active mission found. Checking status... (发现活跃任务，检查状态)")
            self.archive_mission()

        # 3. Decide & Act (决策与行动)
        focus_areas = self._identify_focus_areas(report)

        if not focus_areas:
            print("[Evolution] System stable. No high-priority targets. (系统稳定，无高优先级目标)")
            self._create_maintenance_mission()
        else:
            self._create_foraging_mission(focus_areas)

    def archive_mission(self):
        """Moves active mission to archive with timestamp. (归档活跃任务)"""
        if not os.path.exists(self.active_mission_path):
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"MISSION_{timestamp}.md"
        dest = os.path.join(self.archive_dir, filename)

        shutil.move(self.active_mission_path, dest)
        print(f"[Evolution] Archived previous mission to {filename} (任务已归档)")

    def _identify_focus_areas(self, report) -> List[str]:
        """Selects top 3 priority nodes. (选择前 3 个优先级节点)"""
        focus_areas = []
        # Priority 1: Orphans
        focus_areas.extend(report.orphan_nodes[:3])
        # Priority 2: Stale
        if len(focus_areas) < 3:
            remaining = 3 - len(focus_areas)
            focus_areas.extend(report.stale_nodes[:remaining])

        return focus_areas

    def _create_foraging_mission(self, focus_areas: List[str]):
        """Writes a structured mission file. (生成任务简报)"""
        print(f"[Evolution] Generating mission for targets: {focus_areas} (生成任务)")

        content = [
            "# 🧠 NEXUS CORTEX: Active Mission (活跃任务)",
            f"> Generated (生成时间): {datetime.now().isoformat()}",
            "",
            "## 🎯 Objective (目标)",
            "Close knowledge gaps identified by entropy analysis. (填补熵值分析发现的知识缺口。)",
            "",
            "## 🔍 Targets (目标节点)",
        ]

        for area in focus_areas:
            entity = self.cortex.entities.get(area)
            name = entity.name if entity else area
            desc = entity.desc if entity else "No description available."
            type_ = entity.type if entity else "unknown"

            content.append(f"### 1. {name} (`{area}`)")
            content.append(f"- **Type**: {type_}")
            content.append(f"- **Context**: {desc}")
            content.append("- **Task**: Search for recent developments, integration patterns, or code examples. (搜索最新进展、集成模式或代码示例。)")
            content.append(f"- **Suggested Query**: `latest developments {name} {datetime.now().year}`")
            content.append("")

        content.append("## 📝 Ingestion Protocol (摄入协议)")
        content.append("Run the following to ingest findings: (运行以下命令摄入发现：)")
        content.append("```bash")
        content.append(f"python docs/brain/nexus.py add entity --type concept --id <slug> --name \"<Name>\"")
        content.append(f"python docs/brain/nexus.py connect <source_id> <relation> <target_id>")
        content.append("```")

        with open(self.active_mission_path, "w") as f:
            f.write("\n".join(content))

        print(f"[Evolution] Mission Brief written to {self.active_mission_path}")

    def _create_maintenance_mission(self):
        """Creates a generic exploration mission when no errors exist. (创建维护任务)"""
        content = [
            "# 🧠 NEXUS CORTEX: Exploration Mission (探索任务)",
            f"> Generated (生成时间): {datetime.now().isoformat()}",
            "",
            "## 🎯 Objective (目标)",
            "System is stable. Expand knowledge horizon randomly. (系统稳定，随机扩展知识边界。)",
            "",
            "## 🌌 Suggested Actions (建议行动)",
            "- Explore adjacent fields to existing `tech_stack` nodes. (探索现有技术栈节点的相邻领域。)",
            "- Review `inputs/` folder for unprocessed raw data. (审查 `inputs/` 文件夹中未处理的原始数据。)",
            "- visualize the graph using `nexus visualize`. (使用 `nexus visualize` 可视化图谱。)"
        ]
        with open(self.active_mission_path, "w") as f:
            f.write("\n".join(content))
        print(f"[Evolution] Maintenance Brief written to {self.active_mission_path}")
