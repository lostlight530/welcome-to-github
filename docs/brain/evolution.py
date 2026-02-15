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
        1. Observe: Check entropy.
        2. Orient: Check if current mission is done or stale.
        3. Decide: Generate new mission or keep current.
        4. Act: (Handled by Agent via MISSION_ACTIVE.md)
        """
        print("[Evolution] Starting Cognitive Cycle...")

        # 1. Observe
        self.cortex.load_graph()
        report = self.cortex.analyze_entropy()

        print(f"[Entropy] Density: {report.density:.4f} | Orphans: {len(report.orphan_nodes)} | Stale: {len(report.stale_nodes)}")

        # 2. Orient
        if os.path.exists(self.active_mission_path):
            print("[Evolution] Active mission found. Checking status...")
            # Ideally, we parse the mission file to see if the target nodes are no longer orphans/stale.
            # For now, we'll just Archive it if it's older than 24h to force fresh look
            # Or simplistic approach: Always archive and regenerate to keep it fresh with latest graph state.
            # Let's archive it to history.
            self.archive_mission()

        # 3. Decide & Act (Generate New Mission)
        focus_areas = self._identify_focus_areas(report)

        if not focus_areas:
            print("[Evolution] System stable. No high-priority targets.")
            self._create_maintenance_mission()
        else:
            self._create_foraging_mission(focus_areas)

    def archive_mission(self):
        """Moves active mission to archive with timestamp."""
        if not os.path.exists(self.active_mission_path):
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"MISSION_{timestamp}.md"
        dest = os.path.join(self.archive_dir, filename)

        shutil.move(self.active_mission_path, dest)
        print(f"[Evolution] Archived previous mission to {filename}")

    def _identify_focus_areas(self, report) -> List[str]:
        """Selects top 3 priority nodes."""
        focus_areas = []
        # Priority 1: Orphans
        focus_areas.extend(report.orphan_nodes[:3])
        # Priority 2: Stale
        if len(focus_areas) < 3:
            remaining = 3 - len(focus_areas)
            focus_areas.extend(report.stale_nodes[:remaining])

        return focus_areas

    def _create_foraging_mission(self, focus_areas: List[str]):
        """Writes a structured mission file."""
        print(f"[Evolution] Generating mission for targets: {focus_areas}")

        content = [
            "# 🧠 NEXUS CORTEX: Active Mission",
            f"> Generated: {datetime.now().isoformat()}",
            "",
            "## 🎯 Objective",
            "Close knowledge gaps identified by entropy analysis.",
            "",
            "## 🔍 Targets",
        ]

        for area in focus_areas:
            entity = self.cortex.entities.get(area)
            name = entity.name if entity else area
            desc = entity.desc if entity else "No description available."
            type_ = entity.type if entity else "unknown"

            content.append(f"### 1. {name} (`{area}`)")
            content.append(f"- **Type**: {type_}")
            content.append(f"- **Context**: {desc}")
            content.append("- **Task**: Search for recent developments, integration patterns, or code examples.")
            content.append(f"- **Suggested Query**: `latest developments {name} {datetime.now().year}`")
            content.append("")

        content.append("## 📝 Ingestion Protocol")
        content.append("Run the following to ingest findings:")
        content.append("```bash")
        content.append(f"python docs/brain/nexus.py add entity --type concept --id <slug> --name \"<Name>\"")
        content.append(f"python docs/brain/nexus.py connect <source_id> <relation> <target_id>")
        content.append("```")

        with open(self.active_mission_path, "w") as f:
            f.write("\n".join(content))

        print(f"[Evolution] Mission Brief written to {self.active_mission_path}")

    def _create_maintenance_mission(self):
        """Creates a generic exploration mission when no errors exist."""
        content = [
            "# 🧠 NEXUS CORTEX: Exploration Mission",
            f"> Generated: {datetime.now().isoformat()}",
            "",
            "## 🎯 Objective",
            "System is stable. Expand knowledge horizon randomly.",
            "",
            "## 🌌 Suggested Actions",
            "- Explore adjacent fields to existing `tech_stack` nodes.",
            "- Review `inputs/` folder for unprocessed raw data.",
            "- visualize the graph using `nexus visualize`."
        ]
        with open(self.active_mission_path, "w") as f:
            f.write("\n".join(content))
        print(f"[Evolution] Maintenance Brief written to {self.active_mission_path}")

if __name__ == "__main__":
    root = "docs/brain"
    if len(sys.argv) > 1:
        root = sys.argv[1]

    evolver = Evolver(root)
    evolver.run_cycle()
