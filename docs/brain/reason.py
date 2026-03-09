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
        self.cortex = Cortex(self.brain_path / "cortex.db")

    def ponder(self):
        """
        The Cognitive Loop: Analyzes the Knowledge Graph for patterns,
        risks, and hidden connections.
        """
        print("🤔 NEXUS is pondering...")
        insights = []

        # 1. 结构完整性分析 (Structural Integrity)
        orphans = self._find_orphans()
        if orphans:
            insights.append(f"⚠️  **Isolation Risk**: Found disconnected knowledge nodes. (e.g., {orphans[0]})")

        # 2. 循环依赖检测 (Cycle Detection - Simplified)
        cycles = self._detect_cycles()
        if cycles:
            insights.append(f"🔄 **Circular Logic**: Detected {len(cycles)} potential infinite loops in thinking/code.")

        # 3. 跨域联想 (Cross-Domain Inference)
        bridges = self._find_bridges()
        for bridge in bridges:
            insights.append(f"💡 **Insight**: '{bridge['source']}' implies '{bridge['target']}' via '{bridge['via']}'.")

        # 4. 熵值健康度 (Entropy Check)
        stats = self.cortex.get_stats()
        if stats['density'] < 1.0:
            insights.append("📉 **Cognitive Thinning**: Graph density is low. Needs more connection building.")

        return insights

    def _find_orphans(self):
        """Find entities with 0 relations (Lonely thoughts)"""
        cursor = self.cortex.conn.cursor()
        sql = '''
            SELECT e.name FROM entities e
            LEFT JOIN relations r1 ON e.id = r1.source
            LEFT JOIN relations r2 ON e.id = r2.target
            WHERE r1.source IS NULL AND r2.target IS NULL
            LIMIT 3
        '''
        return [row[0] for row in cursor.execute(sql).fetchall()]

    def _detect_cycles(self):
        """Detect A->B->A patterns (Cognitive Traps)"""
        cursor = self.cortex.conn.cursor()
        # Finding direct reciprocity (A->B and B->A)
        sql = '''
            SELECT r1.source, r1.target
            FROM relations r1
            JOIN relations r2 ON r1.source = r2.target AND r1.target = r2.source
            WHERE r1.source < r1.target -- Avoid duplicates
            LIMIT 3
        '''
        return [f"{row[0]} <-> {row[1]}" for row in cursor.execute(sql).fetchall()]

    def _find_bridges(self):
        """
        Transitive Inference: If A->B (is_a) and B->C (requires),
        then logic suggests A might require C.
        """
        cursor = self.cortex.conn.cursor()
        sql = '''
            SELECT r1.source, r2.target, r1.target
            FROM relations r1
            JOIN relations r2 ON r1.target = r2.source
            WHERE r1.relation = 'defines' AND r2.relation = 'inherits_from'
            LIMIT 3
        '''
        # Logic: If File A defines Class B, and Class B inherits from Class C -> File A depends on Class C
        results = []
        for row in cursor.execute(sql).fetchall():
            results.append({'source': row[0], 'target': row[1], 'via': row[2]})
        return results
