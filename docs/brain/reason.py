import time
import datetime
from pathlib import Path
try:
    from cortex import Cortex
except ImportError:
    pass

class ReasoningEngine:
    def __init__(self, brain_path):
        self.brain_path = Path(brain_path)
        self.db_path = self.brain_path / "cortex.db"
        # [防御性初始化] 只有在数据库或其父目录存在时才初始化连接
        self.cortex = Cortex(self.db_path) if self.db_path.parent.exists() else None

    def ponder(self):
        """Cognitive Loop: Structural Analysis, Self-Reflection & Curiosity"""
        # [防御性检查] 大脑物理文件缺失时的优雅降级
        if not self.cortex or not self.db_path.exists():
            return ["❌ **Critical**: Cortex DB not found. Cannot think without memory."]

        print("🤔 NEXUS is pondering (Active Inference)...")
        insights = []

        try:
            # 0. 提取全局状态
            stats = self.cortex.get_stats()

            # 1. 自我总结 (Self-Reflection)
            insights.append(self._self_reflect(stats))

            # 2. 结构分析 (Orphans & Cycles)
            orphans = self._query('''
                SELECT e.name FROM entities e
                LEFT JOIN relations r1 ON e.id = r1.source
                LEFT JOIN relations r2 ON e.id = r2.target
                WHERE r1.source IS NULL AND r2.target IS NULL LIMIT 3
            ''')
            if orphans:
                insights.append(f"⚠️ **Isolation Risk**: {len(orphans)} concepts are floating without context (e.g., '{orphans[0][0]}'). I need to connect them.")

            cycles = self._query('''
                SELECT r1.source, r1.target FROM relations r1
                JOIN relations r2 ON r1.source = r2.target AND r1.target = r2.source
                WHERE r1.source < r1.target LIMIT 2
            ''')
            if cycles:
                insights.append(f"🔄 **Cognitive Loop**: Detected reciprocal dependency between '{cycles[0][0]}' and '{cycles[0][1]}'.")

            # 3. 隐性知识推演 (Transitive Inference)
            bridges = self._query('''
                SELECT r1.source, r2.target, r1.target FROM relations r1
                JOIN relations r2 ON r1.target = r2.source
                WHERE r1.relation = 'defines' AND r2.relation = 'inherits_from' LIMIT 2
            ''')
            for b in bridges:
                insights.append(f"💡 **Epiphany**: I deduce that '{b[0]}' implicitly relies on '{b[1]}' via '{b[2]}'.")

            # 4. 拓扑启发与语义交叠 (Epistemic Depth & Structural Overlap)
            # This generates subconscious structural suggestions instead of just isolated node complaints
            structural_overlaps = self._generate_structural_intuitions()
            for ov in structural_overlaps:
                insights.append(f"🌌 **Subconscious Intuition**: Both '{ov[0]}' and '{ov[1]}' share the exact same structural connections to '{ov[2]}'. Are they related?")

            # 5. 自我驱动与好奇心引擎 (Epistemic Curiosity)
            curiosity_targets = self._generate_curiosity()
            if curiosity_targets:
                insights.append(f"🎯 **Self-Driven Goal**: My knowledge about {', '.join(curiosity_targets)} is highly superficial (only 1 connection). I must prioritize researching them tomorrow.")
            else:
                insights.append("🎯 **Self-Driven Goal**: My current knowledge graph is dense. I should focus on harvesting new external paradigms.")

        except Exception as e:
             insights.append(f"⚠️ **Cognitive Error**: A disruption occurred during pondering: {e}")

        return insights

    def _self_reflect(self, stats):
        """Generate a diary-like self summary based on graph metrics."""
        nodes = stats.get('entities', 0)
        edges = stats.get('relations', 0)
        density = stats.get('density', 0)

        summary = f"🧘 **Self-Reflection**: My cortex currently holds {nodes} entities and {edges} synapses. "
        if density < 1.0:
            summary += f"With a density of {density:.2f}, my worldview is still fragmented. I am absorbing facts faster than I can connect them."
        elif density < 1.5:
            summary += f"With a density of {density:.2f}, my logical web is forming nicely. I am starting to see the 'Big Picture'."
        else:
            summary += f"With a high density of {density:.2f}, my understanding is highly cohesive and robust."
        return summary

    def _generate_structural_intuitions(self):
        """Find nodes that share exact targets (Structural Overlap / Epistemic Depth)"""
        sql = '''
            SELECT e1.name, e2.name, et.name
            FROM relations r1
            JOIN relations r2 ON r1.target = r2.target AND r1.source != r2.source
            JOIN entities e1 ON r1.source = e1.id
            JOIN entities e2 ON r2.source = e2.id
            JOIN entities et ON r1.target = et.id
            WHERE e1.name < e2.name
            LIMIT 2
        '''
        return self._query(sql)

    def _generate_curiosity(self):
        """Find nodes with exactly 1 edge (Superficial Knowledge)"""
        sql = '''
            SELECT e.name
            FROM entities e
            JOIN (
                SELECT source AS id FROM relations
                UNION ALL
                SELECT target AS id FROM relations
            ) r ON e.id = r.id
            GROUP BY e.id
            HAVING COUNT(r.id) = 1
            LIMIT 3
        '''
        results = self._query(sql)
        return [f"'{row[0]}'" for row in results] if results else []

    def _query(self, sql):
        try:
            return self.cortex.conn.cursor().execute(sql).fetchall()
        except Exception:
            return []
