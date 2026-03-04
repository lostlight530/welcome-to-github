import sys
import os
import shutil
import glob
import random
from datetime import datetime, timedelta
from typing import List, Optional, Tuple
import pathlib

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
        self.inputs_dir = os.path.join(root_dir, "inputs")

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
        # Check for new inputs (Intelligence Sniffer)
        new_inputs = self._check_new_inputs()

        focus_areas = self._identify_focus_areas(report)

        # Determine Cross-Pollination Candidates
        pollination_pair = self._find_cross_pollination_candidates()

        # Determine Transitive Inference (Subconscious Guesses)
        intuitions = self._incubate_ideas()

        if not focus_areas and not new_inputs and not pollination_pair and not intuitions:
            print("[Evolution] System stable. No high-priority targets. (系统稳定，无高优先级目标)")
            self._create_maintenance_mission()
        else:
            self._create_foraging_mission(focus_areas, new_inputs, pollination_pair, intuitions)

        # 4. Generate Auto-Synthesis Report
        self._generate_synthesis_report()

    def archive_mission(self):
        """Moves active mission to archive with timestamp. (归档活跃任务)"""
        if not os.path.exists(self.active_mission_path):
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"MISSION_{timestamp}.md"
        dest = os.path.join(self.archive_dir, filename)

        shutil.move(self.active_mission_path, dest)
        print(f"[Evolution] Archived previous mission to {filename} (任务已归档)")

    def _check_new_inputs(self) -> List[str]:
        """Scans inputs directory for processing, strictly IGNORING the 'archive' folder."""
        recent_files = []
        now = datetime.now()
        threshold = now - timedelta(hours=24)

        base_path = pathlib.Path(self.inputs_dir)
        if not base_path.exists():
            return recent_files

        # 强制只扫描年份目录 (e.g., 2026)，跳过 archive 和其他隐藏文件
        for item in base_path.iterdir():
            if item.is_dir() and item.name.isdigit(): # 只看像 '2026' 这样的年份目录
                for file_path in item.rglob("*.md"):
                    mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                    if mtime > threshold:
                        rel_path = os.path.relpath(str(file_path), self.root_dir)
                        recent_files.append(rel_path)
            elif item.is_file() and item.suffix == ".md":
                mtime = datetime.fromtimestamp(os.path.getmtime(item))
                if mtime > threshold:
                    rel_path = os.path.relpath(str(item), self.root_dir)
                    recent_files.append(rel_path)

        if recent_files:
            print(f"[Evolution] Detected {len(recent_files)} new intelligence briefs. (检测到新情报)")

        return recent_files

    def _identify_focus_areas(self, report) -> List[str]:
        """Selects top 3 priority nodes. (选择前 3 个优先级节点)"""
        focus_areas = []
        focus_areas.extend(report.orphan_nodes[:3])
        if len(focus_areas) < 3:
            remaining = 3 - len(focus_areas)
            focus_areas.extend(report.stale_nodes[:remaining])
        return focus_areas

    def _find_cross_pollination_candidates(self) -> Optional[Tuple[str, str]]:
        """Finds two random, disconnected entities to force a cognitive bridge."""
        if len(self.cortex.entities) < 2:
            return None

        all_ids = list(self.cortex.entities.keys())

        for _ in range(10):
            a, b = random.sample(all_ids, 2)
            has_edge = any(r for r in self.cortex.relations if (r.src == a and r.dst == b) or (r.src == b and r.dst == a))
            if not has_edge:
                return (a, b)

        return None

    def _incubate_ideas(self) -> List[Tuple[str, str, str]]:
        """
        Transitive Inference: If A->B and B->C, guess A->C.
        """
        print("[Evolution] Dreaming of new connections... (潜意识孵化中)")
        guesses = []

        # Build adjacency list for forward and backward traversal
        adj_out = {eid: [] for eid in self.cortex.entities}

        for r in self.cortex.relations:
            adj_out[r.src].append((r.dst, r.rel))

        # Search for A -> B -> C paths
        found_pairs = set()

        for a in self.cortex.entities:
            for b, rel_ab in adj_out.get(a, []):
                for c, rel_bc in adj_out.get(b, []):
                    if a == c: continue # Skip cycles

                    # Check if A -> C already exists directly
                    has_direct = any(r for r in self.cortex.relations if r.src == a and r.dst == c)

                    if not has_direct and (a, c) not in found_pairs:
                        # Avoid purely hierarchical noise
                        if rel_ab != 'is_a' and rel_bc != 'is_a':
                            guesses.append((a, b, c))
                            found_pairs.add((a, c))
                            if len(guesses) >= 3:
                                return guesses
        return guesses

    def _create_foraging_mission(self, focus_areas: List[str], new_inputs: List[str], pollination: Optional[Tuple[str, str]], intuitions: List[Tuple[str, str, str]]):
        """Writes a structured mission file. (生成任务简报)"""
        print(f"[Evolution] Generating mission... (生成任务)")

        content = [
            "# 🧠 NEXUS CORTEX: Active Mission (活跃任务)",
            f"> Generated (生成时间): {datetime.now().isoformat()}",
            "",
            "## 🎯 Objective (目标)",
            "Ingest intelligence, close gaps, and evaluate subconscious intuitions.",
            ""
        ]

        # Section 1: New Intelligence
        if new_inputs:
            content.append("## 📥 Pending Intelligence (待处理情报)")
            content.append("> Priority: Critical (Please review immediately)")
            for inp in new_inputs:
                content.append(f"### 📄 `{inp}`")
                try:
                    with open(os.path.join(self.root_dir, inp), 'r') as f:
                        text = f.read()
                        if "🔥 HIGH VELOCITY ALERT" in text:
                            content.append("- **🔥 ALERT**: High velocity update rate detected.")
                        if "BREAKING CHANGE" in text:
                            content.append("- **⚠️ ALERT**: Contains BREAKING CHANGE.")
                        if "🚨" in text:
                            content.append("- **🚨 ALERT**: Critical Security/Stability Update.")
                except: pass
                content.append("- **Action**: Read file and extract entities.")
                content.append(f"- **Command**: `nexus.py add entity ...`")
                content.append("")

        # Section 2: Transitive Intuitions (The Dream State)
        if intuitions:
            content.append("## 🔮 Subconscious Intuitions (潜意识推演)")
            content.append("> System deduced these via transitive logic (A -> B -> C). Are they valid?")
            for a, b, c in intuitions:
                name_a = self.cortex.entities[a].name
                name_b = self.cortex.entities[b].name
                name_c = self.cortex.entities[c].name
                content.append(f"### ❓ Hypothesis: `{name_a}` -> `{name_c}` ?")
                content.append(f"- **Path**: {name_a} -> {name_b} -> {name_c}")
                content.append(f"- **Action**: If valid, connect them: `nexus.py connect {a} <relation> {c}`")
                content.append("")

        # Section 3: Cross-Pollination
        if pollination:
            a, b = pollination
            name_a = self.cortex.entities[a].name
            name_b = self.cortex.entities[b].name
            content.append("## 🌌 Cross-Pollination (跨界连接)")
            content.append(f"### ? `{name_a}` <--> `{name_b}`")
            content.append(f"- **Entity 1**: {name_a} ({self.cortex.entities[a].type})")
            content.append(f"- **Entity 2**: {name_b} ({self.cortex.entities[b].type})")
            content.append("- **Prompt**: Is there a hidden synergy or conflict?")
            content.append(f"- **Action**: If a link exists: `nexus.py connect {a} <relation> {b}`")
            content.append("")

        # Section 4: Entropy Targets
        if focus_areas:
            content.append("## 🔍 Entropy Targets (熵值目标 - 需强化)")
            content.append("> These nodes have low weight/connections. Touch them to reinforce, or expand them.")
            for area in focus_areas:
                entity = self.cortex.entities.get(area)
                name = entity.name if entity else area
                weight = entity.weight if entity else 0.0
                content.append(f"### 1. {name} (`{area}`)")
                content.append(f"- **Weight**: {weight:.2f}")
                content.append("- **Action**: `nexus.py activate {area}` or search for updates.")
                content.append("")

        content.append("## 📝 Commands")
        content.append("```bash")
        content.append("python docs/brain/nexus.py activate <id>")
        content.append("python docs/brain/nexus.py connect <src> <rel> <dst>")
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
            "- Explore adjacent fields to existing `tech_stack` nodes.",
            "- visualize the graph using `nexus visualize`."
        ]
        with open(self.active_mission_path, "w") as f:
            f.write("\n".join(content))
        print(f"[Evolution] Maintenance Brief written to {self.active_mission_path}")

    def _generate_synthesis_report(self):
        """Generates an automated daily Scholar Synthesis Report based on recent changes."""
        # A simple synthesis logic: summarize new nodes added in the last 24h.
        now = datetime.now()
        threshold = now - timedelta(hours=24)

        new_entities = []
        for eid, entity in self.cortex.entities.items():
            try:
                if entity.updated_at:
                    dt = datetime.fromisoformat(entity.updated_at.replace('Z', '+00:00'))
                    if dt.tzinfo is None: dt = dt.replace(tzinfo=None)
                    if dt > threshold:
                        new_entities.append(entity)
            except Exception:
                pass

        if not new_entities:
            print("[Scholar] No significant new concepts to synthesize today.")
            return

        date_str = now.strftime("%Y%m%d")
        report_filename = f"{date_str}-scholar-synthesis.md"
        report_path = os.path.join(self.memories_dir, report_filename)

        content = [
            f"# 🧠 Scholar Auto-Synthesis Report",
            f"**Date**: {now.strftime('%Y-%m-%d')}",
            f"**Agent**: NEXUS CORTEX (Auto-Scholar)",
            "",
            "## 🌌 Daily Intelligence Summary",
            f"The system ingested **{len(new_entities)}** new entities in the last 24 hours.",
            "",
            "### 📌 Newly Acquired Concepts:"
        ]

        for e in new_entities:
            content.append(f"- **{e.name}** (`{e.type}`): {e.desc}")

        content.append("")
        content.append("## 🤖 Architect's Note")
        content.append("This report is automatically generated by the OODA loop to track cognitive growth.")

        with open(report_path, "w") as f:
            f.write("\n".join(content))

        print(f"[Scholar] Auto-Synthesis Report written to {report_path}")
