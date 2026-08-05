import os
import shutil
import datetime
import logging
import re
from pathlib import Path
from cortex import Cortex
try:
    from reason import ReasoningEngine
except ImportError:
    pass

logging.basicConfig(level=logging.INFO, format='[Evolution] %(message)s')

class Evolver:
    def __init__(self, brain_path):
        self.brain_path = Path(brain_path)
        self.cortex = Cortex(self.brain_path / "cortex.db")
        self.memories_path = self.brain_path / "memories"
        self.inputs_path = self.brain_path / "inputs"

    def run_daily_cycle(self):
        try:
            logging.info("Starting Daily Evolution Cycle... / 启动每日演化周期...")

            # 0. AST Hot-Patching (Genetic Auto-Recombination)
            self._genetic_auto_recombination()

            # 1. Rebuild ephemeral index from JSONL ledger
            self.cortex._init_db()

            # 2. Resolve isolation
            self.cortex.suture_orphans()

            # 3. Process new inputs (Harvester)
            # 4. Cognitive Reflection
            metrics = self.cortex.get_dashboard_metrics()
            orphans = self.cortex.get_orphans(limit=10)

            # 5. Render active dashboard
            self._trigger_render(metrics, orphans)

            # 6. Archive processed inputs
            self._archive_inputs()

            logging.info("Cycle Complete. / 周期完成。")
        except Exception as e:
            logging.error(f"Cycle failed / 周期失败: {e}")
            raise

    def _trigger_render(self, metrics, orphans):
        try:
            r = ReasoningEngine(self.brain_path)
            # Pass isolated nodes names
            isolated_nodes = [o['name'] for o in orphans]
            r._render_daily_archives(metrics, isolated_nodes)
        except Exception as e:
            logging.error(f"Render failed / 渲染失败: {e}")
            raise

    def _genetic_auto_recombination(self):
        """Phase VI: Preparatory State AST Mutator"""
        logging.info("Initiating Genetic Auto-Recombination (AST Mutator)... / 启动基因自动重组 (AST 变异)...")
        logging.info("SYSTEM STATUS: Preparatory State Locked. / 系统状态：预备状态已锁定。")
        logging.info("Writeback Success Rate locked at 0.00% to prevent Ouroboros loop. / 回写成功率锁定在 0.00% 以防止衔尾蛇循环。")

        target_file = self.brain_path / "evolution.py"
        try:
            with open(target_file, "r", encoding="utf-8") as f:
                source = f.read()

            import ast
            tree = ast.parse(source)

            # Define a simple mutator that finds _genetic_auto_recombination and does a null operation
            class SelfMutator(ast.NodeTransformer):
                def visit_FunctionDef(self, node):
                    if node.name == '_genetic_auto_recombination':
                        # Example sandbox operation: Just append a benign pass statement
                        if not any(isinstance(stmt, ast.Pass) for stmt in node.body):
                            node.body.append(ast.Pass())
                    return self.generic_visit(node)

            mutated_tree = SelfMutator().visit(tree)
            ast.fix_missing_locations(mutated_tree)

            # Verify compilation in sandbox before any writes
            compile(mutated_tree, filename="<ast>", mode="exec")
            logging.info("AST Mutation Sandbox check passed. (Physical write bypassed). / AST 变异沙盒检查通过。（已跳过物理写入）。")

        except Exception as e:
            logging.error(f"Genetic Recombination Failed / 基因重组失败: {e}")
            raise

    def _incubate_ideas(self):
        try:
            r = ReasoningEngine(self.brain_path)
            insights = r.ponder()
            return insights
        except Exception as e:
            logging.error(f"Failed to ponder / 推演失败: {e}")
            return []

    def _scan_inputs(self):
        files = []
        if self.inputs_path.exists():
            for f in self.inputs_path.iterdir():
                if f.is_file() and f.name.endswith(".md") and not f.name.startswith('.'):
                    files.append(f)
        return files

    @staticmethod
    def _move_to_archive(source, destination):
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            if source.read_bytes() != destination.read_bytes():
                raise FileExistsError(f"archive collision: {destination}")
            source.unlink()
            return
        os.replace(source, destination)

    def _archive_inputs(self):
        now = datetime.datetime.now()
        archive_dir = self.inputs_path / "archive" / f"{now.year}" / f"{now.month:02d}"
        archive_dir.mkdir(parents=True, exist_ok=True)

        for f in self.inputs_path.iterdir():
            if (
                f.is_file()
                and f.name.endswith(".md")
                and not f.name.startswith(".")
                and f.name != "ARCHIVE_AND_HARVESTER.md"
            ):
                self._move_to_archive(f, archive_dir / f.name)
