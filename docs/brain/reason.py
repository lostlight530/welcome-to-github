# [FILE: docs/brain/reason.py]
import json
import time
from pathlib import Path
try:
    from cortex import Cortex
except ImportError:
    pass

class ReasoningEngine:
    def __init__(self, brain_path):
        self.brain_path = Path(brain_path)
        self.db_path = self.brain_path / "cortex.db"
        self.cortex = Cortex(self.db_path) if self.db_path.parent.exists() else None

    def ponder(self):
        """
        The Cognitive Loop: Analyzes the Knowledge Graph for patterns,
        risks, and hidden connections.
        """
        if not self.cortex:
            return ["❌ **Critical**: Cortex DB not found. Cannot think without memory."]

        print("🤔 NEXUS is pondering (Graph Inference)...")
        insights = []

        # 1. Structural Integrity (Orphans)
        orphans = self._find_orphans()
        if orphans:
            insights.append(f"⚠️  **Isolation Risk**: Found {len(orphans)} disconnected nodes (e.g., {orphans[0]}).")

        # 2. Circular Logic (Loops)
        cycles = self._detect_cycles()
        if cycles:
            insights.append(f"🔄 **Circular Logic**: Detected {len(cycles)} potential infinite loops (e.g., {cycles[0]}).")

        # 3. Transitive Inference (Hidden Bridges)
        # Logic: If A defines B, and B inherits C -> A depends on C
        bridges = self._find_bridges()
        for bridge in bridges:
            insights.append(f"💡 **Inference**: '{bridge['source']}' implicitly relies on '{bridge['via']}' (Concept: {bridge['target']}).")

        # 4. Entropy Check
        stats = self.cortex.get_stats()
        density = stats.get('density', 0)
        insights.append(f"🧠 **Mental State**: Density {density:.2f}. { 'High cohesion.' if density > 1.2 else 'Fragmented.'}")

        return insights

    def _find_orphans(self):
        cursor = self.cortex.conn.cursor()
        sql = '''SELECT e.name FROM entities e LEFT JOIN relations r1 ON e.id = r1.source LEFT JOIN relations r2 ON e.id = r2.target WHERE r1.source IS NULL AND r2.target IS NULL LIMIT 3'''
        return [row[0] for row in cursor.execute(sql).fetchall()]

    def _detect_cycles(self):
        cursor = self.cortex.conn.cursor()
        sql = '''SELECT r1.source, r1.target FROM relations r1 JOIN relations r2 ON r1.source = r2.target AND r1.target = r2.source WHERE r1.source < r1.target LIMIT 1'''
        rows = cursor.execute(sql).fetchall()
        return [f"{r[0]} <-> {r[1]}" for r in rows]

    def _find_bridges(self):
        cursor = self.cortex.conn.cursor()
        sql = '''SELECT r1.source, r2.target, r1.target FROM relations r1 JOIN relations r2 ON r1.target = r2.source WHERE r1.relation = 'defines' AND r2.relation = 'inherits_from' LIMIT 3'''
        results = []
        for row in cursor.execute(sql).fetchall():
            results.append({'source': row[0], 'target': row[1], 'via': row[2]})
        return results
