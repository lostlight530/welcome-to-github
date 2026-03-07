import os
import shutil
import datetime
import logging
from pathlib import Path
from cortex import Cortex

logging.basicConfig(level=logging.INFO, format='[Evolution] %(message)s')

class Evolver:
    def __init__(self, brain_path):
        self.brain_path = Path(brain_path)
        self.cortex = Cortex(self.brain_path / "cortex.db")
        self.memories_path = self.brain_path / "memories"
        self.inputs_path = self.brain_path / "inputs"

    def run_daily_cycle(self):
        logging.info("Starting Daily Evolution Cycle...")
<<<<<<< HEAD

        # 1. Sleep Phase: Decay
        self.cortex.decay_memories()

=======

        # 1. Sleep Phase: Decay
        self.cortex.decay_memories()

>>>>>>> origin/main
        # 2. Dream Phase: Incubate Intuitions
        intuitions = self._incubate_ideas()

        # 3. Orient Phase: Scan Inputs
        new_inputs = self._scan_inputs()

        # 4. Wake Phase: Generate Mission/Brief
        stats = self.cortex.get_stats()
        orphans = self.cortex.get_orphans()
        self._generate_mission(stats, orphans, new_inputs, intuitions)

        logging.info("Cycle Complete.")

<<<<<<< HEAD
=======
        # 3. Orient Phase: Scan Inputs
        new_inputs = self._scan_inputs()

        # 4. Wake Phase: Generate Mission/Brief
        stats = self.cortex.get_stats()
        orphans = self.cortex.get_orphans()
        self._generate_mission(stats, orphans, new_inputs, intuitions)

        logging.info("Cycle Complete.")

>>>>>>> origin/main
    def _incubate_ideas(self):
        """
        Subconscious Intuition (Transitive Inference).
        Looks for A -> B -> C patterns where A is not connected to C.
        """
        logging.info("Incubating Subconscious Intuitions...")
        intuitions = []
        cursor = self.cortex.conn.cursor()

        # Fetch all relations for in-memory graph traversal
        cursor.execute("SELECT source, target, relation FROM relations")
        relations = cursor.fetchall()

        adj = {}
        for r in relations:
            if r['source'] not in adj: adj[r['source']] = []
            adj[r['source']].append(r['target'])

        # 2-Hop Inference Logic
        count = 0
        for a in adj:
            for b in adj[a]:
                if b in adj:
                    for c in adj[b]:
                        if a == c: continue
                        # Check if A->C already exists
                        if c in adj.get(a, []): continue

                        # Found a missing link (Intuition)
                        try:
                            name_a = self.cortex.get_entity(a)['name']
                            name_b = self.cortex.get_entity(b)['name']
                            name_c = self.cortex.get_entity(c)['name']

                            intuition = (
                                f"### ❓ Hypothesis: `{name_a}` -> `{name_c}` ?\n"
                                f"- **Path**: {name_a} -> {name_b} -> {name_c}\n"
                                f"- **Action**: `nexus.py connect {a} relates_to {c}`"
                            )
                            if intuition not in intuitions:
                                intuitions.append(intuition)
                                count += 1
                        except Exception as e:
                            continue

                        if count >= 3: return intuitions # Limit daily intuitions
        return intuitions

    def _scan_inputs(self):
        # Return list of file paths in inputs/ (excluding archive and temp files)
        files = []
        if self.inputs_path.exists():
            for f in self.inputs_path.iterdir():
                if f.is_file() and not f.name.startswith('.') and f.name.endswith('.md'):
                    files.append(str(f))
        return files

    def archive_inputs(self):
        # Move files from inputs/ to inputs/archive/YYYY/MM
        now = datetime.datetime.now()
        archive_dir = self.inputs_path / "archive" / f"{now.year}" / f"{now.month:02d}"
        archive_dir.mkdir(parents=True, exist_ok=True)
<<<<<<< HEAD

        count = 0
        for f in self.inputs_path.iterdir():
            if f.is_file() and not f.name.startswith('.') and f.name.endswith('.md'):
                shutil.move(str(f), str(archive_dir / f.name))
                count += 1
        logging.info(f"Archived {count} inputs.")

=======

        count = 0
        for f in self.inputs_path.iterdir():
            if f.is_file() and not f.name.startswith('.') and f.name.endswith('.md'):
                shutil.move(str(f), str(archive_dir / f.name))
                count += 1
        logging.info(f"Archived {count} inputs.")

>>>>>>> origin/main
    def _generate_architect_brief(self, new_inputs, intuitions):
        """
        Generate Architect's Daily Brief
        """
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d")
<<<<<<< HEAD

        # Intelligence Sorting
        categories = {
            "🧠 架构情报 (Architecture)": [],
            "⚔️ 竞品雷达 (Competitors)": [],
            "📦 边缘战备 (Edge AI)": [],
            "ℹ️ 其他动态 (General)": []
        }

=======

        # Intelligence Sorting
        categories = {
            "🧠 架构情报 (Architecture)": [],
            "⚔️ 竞品雷达 (Competitors)": [],
            "📦 边缘战备 (Edge AI)": [],
            "ℹ️ 其他动态 (General)": []
        }

>>>>>>> origin/main
        for f in new_inputs:
            fname = os.path.basename(f).lower()
            if any(k in fname for k in ['nexent', 'astron', 'mcp', 'agent']):
                categories["🧠 架构情报 (Architecture)"].append(f)
            elif any(k in fname for k in ['dify', 'cherry', 'langchain']):
                categories["⚔️ 竞品雷达 (Competitors)"].append(f)
            elif any(k in fname for k in ['mindspore', 'mediapipe', 'litert', 'npu', 'edge', 'quantiz']):
                categories["📦 边缘战备 (Edge AI)"].append(f)
            else:
                categories["ℹ️ 其他动态 (General)"].append(f)

        content = [
            f"# 🛡️ NEXUS CORTEX: Architect's Daily Brief",
            f"> **Date**: {date_str} | **Entropy**: {self.cortex.get_stats()['density']:.4f}",
            f"",
            f"## 🚨 昨夜今晨 (System Health)",
            f"- **Status**: 🟢 **ONLINE**",
            f""
        ]

        has_intel = False
        for section, files in categories.items():
            if files:
                has_intel = True
                content.append(f"## {section}")
                for f in files:
<<<<<<< HEAD

=======

>>>>>>> origin/main
                    analysis = ""
                    with open(f, 'r') as md_file:
                        for line in md_file:
                            if line.startswith("> **Analysis**:"):
                                analysis = line.strip()
                                break
<<<<<<< HEAD

=======

>>>>>>> origin/main
                    content.append(f"- **{os.path.basename(f)}**")
                    if analysis:
                        content.append(f"  - {analysis}")
                content.append("")
<<<<<<< HEAD

=======

>>>>>>> origin/main
        if not has_intel:
            content.append("## 🌌 虚空监视 (Void Watch)\n> No significant ecosystem movements.\n")

        if intuitions:
            content.append(f"## 🔮 潜意识推演 (Intuitions)\n> {len(intuitions)} potential connections found.\n")

        # Deep Work Suggestion
        suggestion = "Optimization"
        if categories["🧠 架构情报 (Architecture)"]: suggestion = "Review Architecture PRs"
        elif categories["📦 边缘战备 (Edge AI)"]: suggestion = "Test Edge Operators"
<<<<<<< HEAD

        content.append(f"## 📅 深度工作建议 (Deep Work)\n> **Focus**: {suggestion}\n- [ ] Block 2 hours.")

=======

        content.append(f"## 📅 深度工作建议 (Deep Work)\n> **Focus**: {suggestion}\n- [ ] Block 2 hours.")

>>>>>>> origin/main
        return "\n".join(content)

    def _generate_mission(self, stats, orphans, new_inputs, intuitions):
        self.memories_path.mkdir(parents=True, exist_ok=True)
        filename = self.memories_path / "MISSION_ACTIVE.md"
<<<<<<< HEAD

=======

>>>>>>> origin/main
        # Archive old mission
        if filename.exists():
            archive_name = f"MISSION_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            (self.memories_path / "archive").mkdir(parents=True, exist_ok=True)
            try:
                os.rename(filename, self.memories_path / "archive" / archive_name)
            except OSError: pass

        # Generate Brief
        content = self._generate_architect_brief(new_inputs, intuitions)
<<<<<<< HEAD

=======

>>>>>>> origin/main
        # Append Orphan Targets (Classic feature)
        if orphans:
            content += "\n\n## 🔍 待处理熵值 (Entropy Targets)\n"
            for o in orphans:
                content += f"- **{o['name']}** ({o['id']}): Weight {o['weight']:.2f}\n"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
<<<<<<< HEAD

=======

>>>>>>> origin/main
        logging.info(f"Brief generated: {filename}")

if __name__ == "__main__":
    e = Evolver(Path(__file__).parent)
    e.run_daily_cycle()
