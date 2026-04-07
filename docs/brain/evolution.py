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
        self._genetic_auto_recombination()

        # 1. Sleep: Metabolize & Decay
        self.cortex.decay_memories()

        # 2. Sandbox Verification: Run automated tests before deep cognition
        self._run_sandbox_tests()

        # 3. Dream: Incubate Intuitions & Epistemic Curiosity
        intuitions = self._incubate_ideas()

        # 4. Orient: Scan Inputs
        new_inputs = self._scan_inputs()

        # 5. Wake: Generate Strategic Brief
        stats = self.cortex.get_stats()
        orphans = self.cortex.get_orphans()
        self._generate_mission(stats, orphans, new_inputs, intuitions)

        # 6. Archive processed inputs
        self._archive_inputs()

        logging.info("Cycle Complete.")

    def _genetic_auto_recombination(self):
        """Phase V: AST Self-Mutation Sandbox"""
        logging.info("Initiating Genetic Auto-Recombination (AST Mutator)...")
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
                        # Example sandbox operation: Just append a benign print statement or docstring
                        if not any(isinstance(stmt, ast.Pass) for stmt in node.body):
                            node.body.append(ast.Pass())
                    return self.generic_visit(node)

            mutated_tree = SelfMutator().visit(tree)
            ast.fix_missing_locations(mutated_tree)

            # Verify compilation in sandbox before any writes
            compile(mutated_tree, filename="<ast>", mode="exec")
            logging.info("AST Mutation Sandbox check passed. (No write performed for safety in this loop)")

        except Exception as e:
            logging.error(f"Genetic Recombination Failed: {e}")

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

    def _incubate_ideas(self):
        try:
            r = ReasoningEngine(self.brain_path)
            insights = r.ponder()
            if insights and "❌ **Critical**" not in insights[0]:
                self._generate_cognitive_report(insights)
            return insights
        except Exception as e:
            logging.error(f"Failed to ponder: {e}")
            return []

    def _generate_cognitive_report(self, insights):
        import string
        now_utc = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        date_prefix = datetime.datetime.now().strftime("%Y%m%d")
        filename = self.memories_path / f"{date_prefix}-cognitive-report.md"

        # Zero-Dependency Template Engine (string.Template)
        report_template = string.Template("""# 🧠 NEXUS CORTEX: Cognitive Report
> **Date**: $now_utc (UTC)
> **Mode**: Phase IV Absolute Determinism

## 🔬 System Entropy & Inference
$insights_list

## ⚡ Directives
- **Action**: Assess orphans and cycles automatically resolved or escalated.
- **Rule**: No LLM intervention allowed. Pure graph math.
""")

        # Format the insights array as a bulleted string
        formatted_insights = "\n".join([f"- {i}" for i in insights])

        # Fill the template
        rendered_content = report_template.substitute(
            now_utc=now_utc,
            insights_list=formatted_insights
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(rendered_content)
        logging.info(f"Cognitive Report generated via Template Engine: {filename}")

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

    def _analyze_file_content(self, filepath):
        """Extract tags from Harvester's analysis block in the MD file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r'> \*\*Analysis\*\*: (.*)', content)
                if match:
                    return match.group(1).strip()
        except:
            pass
        return ""

    def _generate_mission(self, stats, orphans, new_inputs, intuitions):
        # Categorize Intel
        categories = {
            "🧠 架构情报 (Architecture)": [],
            "⚔️ 竞品雷达 (Competitors)": [],
            "📦 边缘战备 (Edge AI)": [],
            "ℹ️ 其他动态 (General)": []
        }

        arch_triggers = ['nexent', 'astron', 'mcp', 'agent', 'protocol']
        comp_triggers = ['dify', 'langchain', 'openai', 'anthropic']
        edge_triggers = ['mindspore', 'mediapipe', 'litert', 'npu', 'arm', 'quantiz', 'vllm']

        for f in new_inputs:
            fname = f.name.lower()
            tags = self._analyze_file_content(f)
            entry = f"- **{f.name}**\n  - > **Analysis**: {tags}" if tags else f"- **{f.name}**"

            if any(t in fname for t in arch_triggers):
                categories["🧠 架构情报 (Architecture)"].append(entry)
            elif any(t in fname for t in comp_triggers):
                categories["⚔️ 竞品雷达 (Competitors)"].append(entry)
            elif any(t in fname for t in edge_triggers):
                categories["📦 边缘战备 (Edge AI)"].append(entry)
            else:
                categories["ℹ️ 其他动态 (General)"].append(entry)

        # Generate Content using Pure String Templates for Absolute Determinism
        import string
        now = datetime.datetime.now().strftime("%Y-%m-%d")

        # Build intel blocks
        intel_blocks = []
        has_intel = False
        for section, items in categories.items():
            if items:
                has_intel = True
                intel_blocks.append(f"## {section}")
                intel_blocks.extend(items)
                intel_blocks.append("")

        if not has_intel:
            intel_blocks.append("## 🌌 虚空监视 (Void Watch)\n> No significant ecosystem movements.\n")

        intel_content = "\n".join(intel_blocks)

        # Smart Deep Work Suggestion
        suggestion = "System Optimization"
        if categories["🧠 架构情报 (Architecture)"]:
            suggestion = "Review Architecture PRs & Protocol Specs"
        elif categories["📦 边缘战备 (Edge AI)"]:
            suggestion = "Edge Inference Benchmarking (vLLM/LiteRT)"
        elif categories["⚔️ 竞品雷达 (Competitors)"]:
            suggestion = "Strategic Analysis of Competitor Updates"

        # Build Cognitive/Entropy content
        cognitive_content = ""
        if intuitions:
            cognitive_content += "\n## 🤔 认知反思 (Cognitive Report)\n"
            cognitive_content += "\n".join([f"- {i}" for i in intuitions])

        entropy_content = ""
        if orphans:
            entropy_content += "\n\n## 🔍 待处理熵值 (Entropy Targets)\n"
            entropy_content += "\n".join([f"- **{o['name']}** ({o['id']}): Weight {o['weight']:.2f}" for o in orphans])

        # Phase IV Deterministic Template
        mission_template = string.Template("""# 🛡️ NEXUS CORTEX: Architect's Daily Brief (Phase IV)
> **Date**: $date | **Entropy Density**: $density | **Entities**: $entities | **Synapses**: $relations
> **Mode**: Absolute Determinism (Zero Internal LLM)

## 🚨 物理核心状态 (System Health)
- **Status**: 🟢 **ONLINE**
- **4D Temporal Graph**: Active
- **Lobotomy Protocol**: Enforced

$intel_content

## 📅 深度工作建议 (Deep Work)
> **Focus**: $suggestion
- [ ] Block 2 hours for uninterrupted deep work.

$cognitive_content$entropy_content
""")

        rendered_mission = mission_template.safe_substitute(
            date=now,
            density=f"{stats.get('density', 0):.4f}",
            entities=stats.get('entities', 0),
            relations=stats.get('relations', 0),
            intel_content=intel_content,
            suggestion=suggestion,
            cognitive_content=cognitive_content,
            entropy_content=entropy_content
        )

        # Write to file
        filename = self.memories_path / "MISSION_ACTIVE.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(rendered_mission)

        logging.info(f"Brief generated: {filename}")
