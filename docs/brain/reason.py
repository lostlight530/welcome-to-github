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

    def ponder(self, evolution_metrics=None):
        """Phase VI Cognitive Loop: Hardcore Quantitative Dashboard Inference"""
        if not self.cortex or not self.db_path.exists():
            return ["❌ **Critical**: Cortex DB not found. Cannot compute without memory."]

        print("📊 NEXUS is compiling Quantitative Dashboard metrics...")
        insights = []

        try:
            dashboard = self.cortex.get_dashboard_metrics()

            # 1. 重复知识压缩率 (Redundant Knowledge Compression Rate)
            comp_rate = dashboard.get('compression_rate', 0.0)
            insights.append(f"🗜️ **Compression Rate**: {comp_rate:.2f}% of the physical ledger is deduplicated temporal history.")

            # 2. 高价值待补全节点 (High-Value Bounty via PageRank)
            bounty_target = self._generate_pagerank_bounty()
            if bounty_target:
                insights.append(f"👑 **Ecosystem Choke Point (PageRank)**: Target `{bounty_target}` possesses maximum mathematical centrality. Priority bounty issued.")

            # 3. 结构性死锁检测 (Structural Deadlock)
            cycles = self._query('''
                SELECT r1.source, r1.target FROM relations r1
                JOIN relations r2 ON r1.source = r2.target AND r1.target = r2.source
                WHERE r1.source < r1.target AND r1.invalid_at IS NULL AND r2.invalid_at IS NULL
                LIMIT 2
            ''')
            if cycles:
                insights.append(f"🔄 **Cognitive Deadlock**: Detected strict reciprocal dependency between '{cycles[0][0]}' and '{cycles[0][1]}'. Requires manual edge pruning.")

            # 4. 语义交叠与桥接推演 (Transitive Bridge & Overlap)
            bridges = self._query('''
                SELECT r1.source, r2.target, r1.target FROM relations r1
                JOIN relations r2 ON r1.target = r2.source
                WHERE r1.relation = 'defines' AND r2.relation = 'inherits_from' AND r1.invalid_at IS NULL AND r2.invalid_at IS NULL
                LIMIT 2
            ''')
            for b in bridges:
                insights.append(f"💡 **Transitive Inference**: Synthesized logical bridge: `{b[0]}` -> `{b[1]}` via `{b[2]}`.")

            # 5. 决策回写成功率 (Decision Writeback Success Rate - provided by evolution layer)
            if evolution_metrics and 'writeback_success_rate' in evolution_metrics:
                wr_rate = evolution_metrics['writeback_success_rate']
                insights.append(f"🛡️ **Writeback Success Rate**: {wr_rate:.2f}% of autonomous sandbox mutations were safely committed.")
            else:
                insights.append("🛡️ **Writeback Success Rate**: Sandbox mutations constrained. 0.00% physical writeback in preparatory state.")

        except Exception as e:
             insights.append(f"⚠️ **Computation Error**: A matrix disruption occurred during pondering: {e}")

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

    def _render_daily_archives(self, stats: dict, isolated_nodes: list):
        """Phase VI: Hardcore Quantitative Dashboard Rendering (Zero-Dependency)."""
        import os
        from datetime import datetime
        from string import Template

        try:
            today_str = datetime.now().strftime("%Y%m%d")
            memories_dir = os.path.join(os.path.dirname(__file__), 'memories')
            os.makedirs(memories_dir, exist_ok=True)

            dashboard = self.cortex.get_dashboard_metrics()
            comp_rate = dashboard.get('compression_rate', 0.0)
            low_conn = dashboard.get('low_connection_nodes', 0)

            # Phase VI Dashboard Template
            cog_tmpl = Template(
                "# 📊 NEXUS CORTEX 量化仪表盘 (Quantitative Dashboard) - $date\n\n"
                "## 📈 核心系统矩阵 (Core System Metrics)\n"
                "- **新增活跃实体数 (Active Entities)**: $nodes\n"
                "- **新增活跃关系数 (Active Relations)**: $edges\n"
                "- **低连接节点数 (Low-Connectivity Nodes)**: $low_conn (Requires structural bridging)\n"
                "- **重复知识压缩率 (Compression Rate)**: $comp_rate%\n"
                "- **拓扑计算密度 (Density)**: $density\n\n"
                "> System running in Absolute Determinism mode. Sentimental narratives deactivated.\n"
            )
            cog_content = cog_tmpl.safe_substitute(
                date=today_str,
                density=f"{stats.get('density', 0):.4f}",
                nodes=stats.get('entities', 0),
                edges=stats.get('relations', 0),
                low_conn=low_conn,
                comp_rate=f"{comp_rate:.2f}"
            )
            with open(os.path.join(memories_dir, f"{today_str}-quantitative-dashboard.md"), 'w', encoding='utf-8') as f:
                f.write(cog_content)

            # MISSION ACTIVE (绝对悬赏令)
            targets_str = "\n".join([f"- [ ] High-Value Target: `{node}`" for node in isolated_nodes[:5]])
            if not targets_str: targets_str = "- [x] Topology optimal. No critical choke points identified."

            mission_tmpl = Template(
                "# 📜 物理悬赏令 (MISSION ACTIVE)\n"
                "> Mathematical Centrality Target Bounties.\n\n"
                "## 🎯 高价值待补全节点 (High-Value Bounty Targets)\n"
                "$targets\n\n"
                "## 🚀 雷达状态 (Radar State)\n"
                "Double-Clutch Anti-Shake enabled. Awaiting rigid updates.\n\n"
                "## 🛡️ 决策回写状态 (Writeback State)\n"
                "Status: Preparatory Shell. Writeback Success Rate: 0.00%. \n"
            )
            mission_content = mission_tmpl.safe_substitute(targets=targets_str)
            with open(os.path.join(memories_dir, "MISSION_ACTIVE.md"), 'w', encoding='utf-8') as f:
                f.write(mission_content)

            print(f"[Reasoning] Engine successfully rendered Quantitative Dashboards via Templates.")
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
