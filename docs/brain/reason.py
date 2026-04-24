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
            # Dashboard Metrics
            metrics = self.cortex.get_dashboard_metrics()

            # 1. 结构分析 (Orphans & Cycles)
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

            # 5. 生态咽喉推演 (PageRank Centrality Bounty)
            bounty_target = self._generate_pagerank_bounty()
            if bounty_target:
                insights.append(f"👑 **Ecosystem Choke Point (PageRank)**: The node '{bounty_target}' has absolute mathematical centrality. Issue highest priority bounty for this node.")

            # 6. 自我驱动与好奇心引擎 (Epistemic Curiosity)
            curiosity_targets = self._generate_curiosity()
            if curiosity_targets:
                insights.append(f"🎯 **Self-Driven Goal**: My knowledge about {', '.join(curiosity_targets)} is highly superficial (only 1 connection). I must prioritize researching them tomorrow.")
            else:
                insights.append("🎯 **Self-Driven Goal**: My current knowledge graph is dense. I should focus on harvesting new external paradigms.")

        except Exception as e:
             insights.append(f"⚠️ **Cognitive Error**: A disruption occurred during pondering: {e}")

        return insights

    def _calculate_pagerank(self, nodes: list, edges: list, iterations: int = 20, damping: float = 0.85) -> dict:
        """Phase V: Pure mathematical centrality deduction without external libraries."""
        try:
            graph = {node: [] for node in nodes}
            for source, target in edges:
                if source in graph:
                    graph[source].append(target)

            n_nodes = len(nodes)
            if n_nodes == 0: return {}

            ranks = {node: 1.0 / n_nodes for node in nodes}
            for _ in range(iterations):
                new_ranks = {node: (1.0 - damping) / n_nodes for node in nodes}
                for node, outbound in graph.items():
                    if outbound:
                        share = (ranks[node] * damping) / len(outbound)
                        for edge in outbound:
                            if edge in new_ranks:
                                new_ranks[edge] += share
                ranks = new_ranks
            return ranks
        except Exception as e:
            print(f"[Reasoning Error] Matrix math failed: {str(e)}")
            return {}

    def _generate_pagerank_bounty(self):
        """Calculate PageRank on the active graph to find the true central hub."""
        nodes_raw = self._query("SELECT id, name FROM entities WHERE invalid_at IS NULL")
        edges_raw = self._query("SELECT source, target FROM relations WHERE invalid_at IS NULL")

        if not nodes_raw or not edges_raw:
            return None

        nodes = [row[0] for row in nodes_raw]
        node_names = {row[0]: row[1] for row in nodes_raw}
        edges = [(row[0], row[1]) for row in edges_raw]

        ranks = self._calculate_pagerank(nodes, edges)

        if not ranks:
            return None

        # Find the node with the highest PageRank
        top_node_id = max(ranks, key=ranks.get)
        return node_names.get(top_node_id, top_node_id)

    def _render_daily_archives(self, metrics: dict, isolated_nodes: list):
        """Phase VI: Hardcore Quantitative Dashboard Rendering (Zero-Dependency)."""
        import os
        from datetime import datetime
        from string import Template

        try:
            today_str = datetime.now().strftime("%Y%m%d")
            memories_dir = os.path.join(os.path.dirname(__file__), 'memories')
            os.makedirs(memories_dir, exist_ok=True)

            # Anchor 1: Quantitative Dashboard (量化仪表盘)
            dash_tmpl = Template(
                "# 📊 NEXUS CORTEX 量化仪表盘 (Quantitative Dashboard) - $date\n\n"
                "## 📈 核心系统指标 (Core System Metrics)\n"
                "| Metric | Value |\n"
                "| :--- | :--- |\n"
                "| Active Entities | $active_entities |\n"
                "| Active Relations | $active_relations |\n"
                "| Compression Rate | $compression_rate |\n"
                "| Low-Connectivity Nodes | $low_connectivity |\n"
            )
            dash_content = dash_tmpl.safe_substitute(
                date=today_str,
                active_entities=metrics.get('active_entities', 0),
                active_relations=metrics.get('active_relations', 0),
                compression_rate=f"{metrics.get('compression_rate', 0.0):.4f}",
                low_connectivity=metrics.get('low_connectivity', 0)
            )
            with open(os.path.join(memories_dir, f"{today_str}-quantitative-dashboard.md"), 'w', encoding='utf-8') as f:
                f.write(dash_content)

            # Anchor 2: MISSION ACTIVE (绝对悬赏令 - SOP)
            # Replaced natural language targets with actionable CLI commands
            targets_str = "\n".join([f"- [ ] Executable SOP: `python docs/brain/nexus.py connect \"{node}\" \"is_capability_of\" \"concept_nexus_system\"`" for node in isolated_nodes[:5]])
            if not targets_str: targets_str = "- [x] Topology optimal. No immediate active inference required."

            # Calculate PageRank Target Hub
            pagerank_hub = self._generate_pagerank_bounty()
            pagerank_str = f"**Cognitive Hub (PageRank)**: `{pagerank_hub}`" if pagerank_hub else "Cognitive Hub: Pending inference."

            mission_tmpl = Template(
                "# 📜 绝对悬赏令 (MISSION ACTIVE)\n"
                "> Standard Operating Procedure (SOP) Automation Checklist.\n\n"
                "## 🎯 监控目标 (Target)\n"
                "$targets\n\n"
                "## 🧠 认知阵眼 (Cognitive Hubs)\n"
                "$pagerank_hub\n\n"
                "## 🚀 新版本发布 (New Release)\n"
                "Awaiting native Harvester ingestion cycle.\n\n"
                "## 🔨 最近提交 (Recent Commits)\n"
                "Awaiting repository sync.\n\n"
                "## 🛡️ 信任评分 (Trust Score)\n"
                "Deterministic Physical Source: 100% (Zero LLM involved).\n\n"
                "## ⚙️ 演化回写率 (Evolution Writeback)\n"
                "Writeback Success Rate: 0.00% (Preparatory State Locked)\n"
            )
            mission_content = mission_tmpl.safe_substitute(
                targets=targets_str,
                pagerank_hub=pagerank_str
            )
            with open(os.path.join(memories_dir, "MISSION_ACTIVE.md"), 'w', encoding='utf-8') as f:
                f.write(mission_content)

            print(f"[Reasoning] Engine successfully rendered Quantitative Dashboard via Templates.")
        except Exception as e:
            print(f"[Reasoning Error] Template enforcement failed: {str(e)}")

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
              AND r1.invalid_at IS NULL AND r2.invalid_at IS NULL
              AND e1.invalid_at IS NULL AND e2.invalid_at IS NULL AND et.invalid_at IS NULL
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
