import sys
import os
import shutil
import json
import glob
from datetime import datetime
from typing import List, Dict, Any

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
        self.inputs_dir = os.path.join(root_dir, "inputs")
        self.archive_dir = os.path.join(self.memories_dir, "archive")
        self.active_mission_path = os.path.join(self.memories_dir, "MISSION_ACTIVE.md")

        os.makedirs(self.archive_dir, exist_ok=True)

    def run_cycle(self):
        """
        The main OODA loop.
        OODA 循环：观察、调整、决策、行动。
        Observe (Observe External + Internal) -> Orient -> Decide -> Act
        """
        print("[Evolution] Starting Cognitive Cycle... (开始认知循环)")

        # 1. Observe (观察：内外部双向感知)
        self.cortex.load_graph()
        internal_report = self.cortex.analyze_entropy()
        external_risks = self._sniff_external_risks()

        print(f"[Entropy] Density (密度): {internal_report.density:.4f} | Orphans (孤岛): {len(internal_report.orphan_nodes)}")
        print(f"[Intelligence] Detected {len(external_risks)} high-risk external signals. (探测到外部风险信号)")

        # 2. Orient (调整)
        if os.path.exists(self.active_mission_path):
            self.archive_mission()

        # 3. Decide & Act (决策与行动：优先级排序)
        # 优先级：外部 BREAKING CHANGE (P0) > 内部孤岛节点 (P1) > 内部陈旧节点 (P2)
        targets = self._identify_priority_targets(external_risks, internal_report)

        if not targets:
            print("[Evolution] System stable. No high-priority targets. (系统稳定，无高优先级目标)")
            self._create_maintenance_mission()
        else:
            self._create_mission_report(targets)

    def _sniff_external_risks(self) -> List[Dict]:
        """Scans the latest candidates.jsonl for BREAKING CHANGE signals."""
        input_files = glob.glob(os.path.join(self.inputs_dir, "candidates_*.jsonl"))
        if not input_files:
            return []

        # 获取最新的情报文件 (Get the most recent harvester output)
        latest_file = max(input_files, key=os.path.getmtime)
        risks = []

        try:
            with open(latest_file, 'r', encoding='utf-8') as f:
                for line in f:
                    data = json.loads(line)
                    # 关键逻辑：嗅探破坏性变更 (Sniffing for BREAKING CHANGE)
                    desc_upper = data.get("desc", "").upper()
                    if "BREAKING CHANGE" in desc_upper:
                        risks.append({
                            "id": data.get("id"),
                            "reason": "🚨 BREAKING CHANGE (破坏性更新)",
                            "name": data.get("name"),
                            "desc": data.get("desc"),
                            "url": data.get("url"),
                            "priority": "P0"
                        })
        except Exception as e:
            print(f"[Error] Failed to sniff risks: {e}")

        return risks

    def _identify_priority_targets(self, external_risks: List[Dict], internal_report) -> List[Dict]:
        """Merges external and internal triggers into a prioritized target list."""
        final_targets = []

        # P0: External Risks (外部风险信号) - Max 3
        final_targets.extend(external_risks[:3])

        # P1: Internal Orphans (内部孤岛节点)
        if len(final_targets) < 3:
            needed = 3 - len(final_targets)
            for eid in internal_report.orphan_nodes[:needed]:
                entity = self.cortex.entities.get(eid)
                final_targets.append({
                    "id": eid,
                    "reason": "🔍 Knowledge Gap (知识孤岛)",
                    "name": entity.name if entity else eid,
                    "desc": entity.desc if entity else "Missing context.",
                    "priority": "P1"
                })

        # P2: Internal Stale Nodes (内部陈旧节点) - If space remains
        if len(final_targets) < 3:
             needed = 3 - len(final_targets)
             for eid in internal_report.stale_nodes[:needed]:
                 entity = self.cortex.entities.get(eid)
                 # Avoid duplicates if node is both orphan and stale
                 if any(t['id'] == eid for t in final_targets):
                     continue
                 final_targets.append({
                    "id": eid,
                    "reason": "🍂 Stale Knowledge (陈旧知识)",
                    "name": entity.name if entity else eid,
                    "desc": entity.desc if entity else "Needs review.",
                    "priority": "P2"
                 })

        return final_targets

    def _create_mission_report(self, targets: List[Dict]):
        """Generates a bilingual, structured mission document."""
        print(f"[Evolution] Generating mission for {len(targets)} priority targets.")

        content = [
            "# 🧠 NEXUS CORTEX: Active Mission (活跃任务)",
            f"> Generated (生成时间): {datetime.now().isoformat()}",
            "",
            "## 🎯 Objective (目标)",
            "Execute defensive upgrades or bridge knowledge gaps. (执行防御性升级或填补知识缺口。)",
            "",
            "## 📋 Targets (目标清单)"
        ]

        for i, t in enumerate(targets, 1):
            priority_icon = "🔴" if t['priority'] == "P0" else "🟡" if t['priority'] == "P1" else "🟢"
            content.append(f"### {i}. {priority_icon} {t['name']} (`{t['priority']}`)")
            content.append(f"- **Trigger (触发原因)**: {t['reason']}")
            content.append(f"- **Context (背景)**: {t['desc']}")

            if t.get('url'):
                content.append(f"- **Reference (参考资料)**: [View on GitHub]({t['url']})")

            action_item = "Audit API compatibility and update local schema." if t['priority'] == "P0" else \
                          "Find connections to existing tech stack nodes." if t['priority'] == "P1" else \
                          "Review entity for updates."

            content.append(f"- **Action Item (行动项)**: {action_item}")
            content.append("")

        content.extend([
            "## 📝 Ingestion Protocol (摄入协议)",
            "Use standard MCP tools to commit new insights: (使用 MCP 工具提交洞察：)",
            "```bash",
            "python docs/brain/nexus.py add entity --id <id> --name \"<name>\"",
            "python docs/brain/nexus.py connect <src> <rel> <dst>",
            "```"
        ])

        with open(self.active_mission_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        print(f"[Evolution] Mission Brief finalized at {self.active_mission_path}")

    def archive_mission(self):
        """Archives previous mission files."""
        if not os.path.exists(self.active_mission_path):
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"MISSION_{timestamp}.md"
        dest = os.path.join(self.archive_dir, filename)
        shutil.move(self.active_mission_path, dest)
        print(f"[Evolution] Archived previous mission to {filename} (任务已归档)")

    def _create_maintenance_mission(self):
        """Standard maintenance when no high-priority targets exist."""
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
            "- Visualize the graph using `nexus visualize`. (使用 `nexus visualize` 可视化图谱。)"
        ]
        with open(self.active_mission_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        print(f"[Evolution] Maintenance Brief written to {self.active_mission_path}")

if __name__ == "__main__":
    Evolver("docs/brain").run_cycle()
