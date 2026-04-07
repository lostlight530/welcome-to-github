import os
import shutil
import datetime
import logging
import re
import subprocess
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
        logging.info("Starting Daily Evolution Cycle...")

        # 0. AST Hot-Patching (Genetic Auto-Recombination)
        evo_metrics = self._genetic_auto_recombination()

        # 1. Sleep: Metabolize & Decay
        self.cortex.decay_memories()

        # 2. Sandbox Verification: Run automated tests before deep cognition
        self._run_sandbox_tests()

        # 3. Dream: Incubate Intuitions & Epistemic Curiosity
        intuitions = self._incubate_ideas(evo_metrics)

        # 4. Orient: Scan Inputs
        new_inputs = self._scan_inputs()

        # 5. Wake: Delegate Render to Reason Engine
        stats = self.cortex.get_stats()
        orphans = self.cortex.get_orphans()

        # Suture orphans automatically
        self.cortex.suture_orphans()

        self._trigger_render(stats, orphans)

        # 6. Archive processed inputs
        self._archive_inputs()

        logging.info("Cycle Complete.")

    def _trigger_render(self, stats, orphans):
        try:
            r = ReasoningEngine(self.brain_path)
            # Pass isolated nodes names
            isolated_nodes = [o['name'] for o in orphans]
            r._render_daily_archives(stats, isolated_nodes)
        except Exception as e:
            logging.error(f"Render failed: {e}")

    def _genetic_auto_recombination(self):
        """Phase VI: Controlled Evolution Preparatory State (可控演化准备态)"""
        logging.info("Initiating Genetic Auto-Recombination (AST Mutator) - PREPARATORY STATE...")
        target_file = self.brain_path / "evolution.py"
        try:
            with open(target_file, "r", encoding="utf-8") as f:
                source = f.read()

            import ast
            tree = ast.parse(source)

            # Define a strict boundary mutator
            class SelfMutator(ast.NodeTransformer):
                def visit_FunctionDef(self, node):
                    if node.name == '_genetic_auto_recombination':
                        # Safe sandbox operation: structural inspection only
                        if not any(isinstance(stmt, ast.Pass) for stmt in node.body):
                            node.body.append(ast.Pass())
                    return self.generic_visit(node)

            mutated_tree = SelfMutator().visit(tree)
            ast.fix_missing_locations(mutated_tree)

            # Strict Sandbox Compilation Check
            compile(mutated_tree, filename="<ast>", mode="exec")

            logging.info("[Safeguard Active] AST Mutation Sandbox check passed.")
            logging.info("System State: Highly conservative boundary. Physical writeback is deliberately disabled.")
            logging.info("Decision writeback success rate intentionally locked at 0.00% to prevent unverified autonomic code mutation.")

            # Return metrics to be consumed by the Reason Engine Dashboard
            return {"writeback_success_rate": 0.0}

        except Exception as e:
            logging.error(f"Genetic Recombination Failed: {e}")
            return {"writeback_success_rate": 0.0}

    def _run_sandbox_tests(self):
        """AST Loop Preparation: Verifies local MCP and systems logic via subprocess."""
        logging.info("Executing Sandbox Verification Protocol...")
        test_script = self.brain_path / "test_mcp.py"
        if test_script.exists():
            try:
                # We strictly only assert (Code 0), keeping safety intact
                result = subprocess.run(
                    ["python", str(test_script)],
                    capture_output=True,
                    text=True,
                    check=True
                )
                logging.info(f"Sandbox Verification Passed: {result.stdout.strip().splitlines()[-1]}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Sandbox Verification Failed! Exit Code {e.returncode}")
                logging.error(e.stderr)
                raise RuntimeError("Sandbox Verification aborted the Evolution Cycle due to protocol failures.") from e

    def _incubate_ideas(self, evo_metrics=None):
        try:
            r = ReasoningEngine(self.brain_path)
            insights = r.ponder(evolution_metrics=evo_metrics)
            return insights
        except Exception as e:
            logging.error(f"Failed to ponder: {e}")
            return []

    def _scan_inputs(self):
        files = []
        if self.inputs_path.exists():
            for f in self.inputs_path.iterdir():
                if f.is_file() and f.name.endswith(".md") and not f.name.startswith('.'):
                    files.append(f)
        return files

    def _archive_inputs(self):
        now = datetime.datetime.now()
        archive_dir = self.inputs_path / "archive" / f"{now.year}" / f"{now.month:02d}"
        archive_dir.mkdir(parents=True, exist_ok=True)

        for f in self.inputs_path.iterdir():
            if f.is_file() and f.name.endswith(".md") and not f.name.startswith('.'):
                shutil.move(str(f), str(archive_dir / f.name))

