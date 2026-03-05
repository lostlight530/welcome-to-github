import os
import logging
import datetime
from pathlib import Path
from typing import List, Dict
from cortex import Cortex

logging.basicConfig(level=logging.INFO, format='[Evolution] %(message)s')

class Evolver:
    def __init__(self, cortex: Cortex):
        self.cortex = cortex
        self.brain_path = Path("docs/brain")
        self.memories_path = self.brain_path / "memories"
        self.memories_path.mkdir(exist_ok=True)

    def run_daily_cycle(self):
        """The Main OODA Loop."""
        logging.info("Starting Cognitive Cycle...")

        # 1. Biological Sleep: Decay old memories first
        self.cortex.decay_memories()

        # 2. Assessment: Calculate Entropy
        density = self._calculate_cognitive_density()
        orphans = self._find_orphans()

        # 3. Subconscious: Dream of new connections (Transitive Inference)
        intuitions = self._incubate_ideas()

        # 4. Perception: Check for new inputs
        new_inputs = self._check_new_inputs()

        # 5. Synthesis: Generate Mission
        if new_inputs or density < 0.1 or intuitions:
            self._generate_mission(density, orphans, new_inputs, intuitions)
        else:
            logging.info("System Stable. No high-entropy action required.")

    def _calculate_cognitive_density(self) -> float:
        """Density = Relations / Entities"""
        cursor = self.cortex.conn.cursor()
        e_count = cursor.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
        r_count = cursor.execute("SELECT COUNT(*) FROM relations").fetchone()[0]

        if e_count == 0: return 0.0
        density = r_count / e_count
        logging.info(f"Density: {density:.4f} (E:{e_count}, R:{r_count})")
        return density

    def _find_orphans(self) -> List[Dict]:
        """Find entities with NO relations (High Entropy)."""
        cursor = self.cortex.conn.cursor()
        sql = '''
            SELECT * FROM entities
            WHERE id NOT IN (SELECT source FROM relations)
            AND id NOT IN (SELECT target FROM relations)
            LIMIT 5
        '''
        cursor.execute(sql)
        return [dict(row) for row in cursor.fetchall()]

    def _incubate_ideas(self) -> List[str]:
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
                        except:
                            continue

                        if count >= 3: return intuitions # Limit daily intuitions
        return intuitions

    def _check_new_inputs(self) -> List[str]:
        """Check inputs/ folder for fresh md files."""
        input_dir = self.brain_path / "inputs"
        new_files = []
        for root, _, files in os.walk(input_dir):
            if "archive" in root: continue
            for f in files:
                if f.endswith(".md"):
                    new_files.append(os.path.join(root, f))
        return new_files

    def _generate_mission(self, density, orphans, new_inputs, intuitions):
        """Write the daily mission file."""
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        timestamp = datetime.datetime.now().isoformat()

        filename = self.memories_path / "MISSION_ACTIVE.md"

        # Archiving logic
        if filename.exists():
            archive_name = f"MISSION_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            archive_path = self.memories_path / "archive" / archive_name
            archive_path.parent.mkdir(parents=True, exist_ok=True)
            filename.rename(archive_path)

        content = [
            f"# 🧠 NEXUS CORTEX: Active Mission",
            f"> Generated: {timestamp}",
            f"",
            f"## 🎯 Objective",
            f"Ingest intelligence, close gaps, and evaluate subconscious intuitions.",
            f"",
        ]

        if new_inputs:
            content.append(f"## 📥 Pending Intelligence")
            content.append(f"> Priority: Critical")
            for f in new_inputs:
                rel_path = os.path.relpath(f, self.brain_path)
                content.append(f"### 📄 `{rel_path}`")
                content.append(f"- **Action**: Read and extract entities.")
                content.append(f"- **Command**: `nexus.py add entity ...`")
            content.append("")

        if intuitions:
            content.append(f"## 🔮 Subconscious Intuitions")
            content.append(f"> System deduced these via transitive logic (A -> B -> C).")
            for item in intuitions:
                content.append(item)
            content.append("")

        if orphans:
            content.append(f"## 🔍 Entropy Targets")
            content.append(f"> Isolate nodes found. Connect or Prune.")
            for o in orphans:
                content.append(f"### 1. {o['name']} (`{o['id']}`)")
                content.append(f"- **Weight**: {o.get('weight', 1.0):.2f}")
                content.append(f"- **Action**: `nexus.py activate {o['id']}`")
            content.append("")

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(content))

        logging.info(f"Mission generated: {filename}")

if __name__ == "__main__":
    c = Cortex("docs/brain/cortex.db")
    e = Evolver(c)
    e.run_daily_cycle()
