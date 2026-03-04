#!/usr/bin/env python3
import argparse
import sys
import os
import shutil
import glob
import pathlib
from datetime import datetime

# Add current directory to path so imports work
# 将当前目录添加到路径，以便导入工作
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cortex import Cortex
from factory import KnowledgeFactory
from evolution import Evolver

def clean_cache(root_dir: str):
    """
    Cleans __pycache__ and temporary files.
    清除 __pycache__ 和临时文件。
    """
    print(f"[Nexus] Cleaning cache in {root_dir}...")
    dirs_to_remove = ["__pycache__", ".pytest_cache", ".mypy_cache", "build", "dist"]
    for pattern in dirs_to_remove:
        for p in glob.glob(os.path.join(root_dir, "**", pattern), recursive=True):
            try:
                shutil.rmtree(p)
                print(f"  - Removed Dir: {p}")
            except Exception as e:
                print(f"  ! Failed to remove dir {p}: {e}")
    files_to_remove = ["*.pyc", "*.pyo", "*.pyd", ".DS_Store", "*.tmp", "*.log"]
    for pattern in files_to_remove:
        for p in glob.glob(os.path.join(root_dir, "**", pattern), recursive=True):
            try:
                os.remove(p)
                print(f"  - Removed File: {p}")
            except Exception as e:
                print(f"  ! Failed to remove file {p}: {e}")
    print("[Nexus] Cache clean complete. (缓存清理完成)")

def archive_inputs(root_dir: str):
    """
    Moves processed files from inputs/YYYY/MM to inputs/archive/YYYY/MM.
    """
    root_input = pathlib.Path(root_dir) / "inputs"
    archive_root = root_input / "archive"

    moved_count = 0

    if not root_input.exists():
        print("✅ No inputs directory found.")
        return

    for year_dir in root_input.iterdir():
        if year_dir.is_dir() and year_dir.name.isdigit(): # e.g., 2026
            for month_dir in year_dir.iterdir():
                if month_dir.is_dir(): # e.g., 02
                    target_dir = archive_root / year_dir.name / month_dir.name
                    target_dir.mkdir(parents=True, exist_ok=True)

                    for md_file in month_dir.glob("*.md"):
                        shutil.move(str(md_file), str(target_dir / md_file.name))
                        print(f"📦 Archived: {md_file.name}")
                        moved_count += 1

    if moved_count == 0:
        print("✅ No files to archive. Workspace clean.")
    else:
        print(f"🧹 Cleaned up {moved_count} files.")

def main():
    parser = argparse.ArgumentParser(description="NEXUS CORTEX: Cognitive Synthesis Protocol CLI")
    parser.add_argument("--root", default="docs/brain", help="Path to brain root directory")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Existing commands
    status_parser = subparsers.add_parser("status", help="Show cognitive entropy report")
    search_parser = subparsers.add_parser("search", help="Search for concepts")
    search_parser.add_argument("query", help="Search term")
    viz_parser = subparsers.add_parser("visualize", help="Generate Mermaid.js graph")
    evolve_parser = subparsers.add_parser("evolve", help="Run the OODA evolution cycle")

    connect_parser = subparsers.add_parser("connect", help="Connect two concepts")
    connect_parser.add_argument("src", help="Source Entity ID")
    connect_parser.add_argument("rel", help="Relation")
    connect_parser.add_argument("dst", help="Destination Entity ID")
    connect_parser.add_argument("--context", default="", help="Context/Source")

    add_parser = subparsers.add_parser("add", help="Add a new entity")
    add_parser.add_argument("category", help="Category/File")
    add_parser.add_argument("--id", required=True, help="Unique ID slug")
    add_parser.add_argument("--type", required=True, help="Type")
    add_parser.add_argument("--name", required=True, help="Human readable name")
    add_parser.add_argument("--desc", required=True, help="Description")
    add_parser.add_argument("--tags", help="Comma-separated tags")

    touch_parser = subparsers.add_parser("touch", help="Legacy touch. Routes to activate.")
    touch_parser.add_argument("id", help="Entity ID to touch")

    activate_parser = subparsers.add_parser("activate", help="Activate a memory to strengthen its neural weight")
    activate_parser.add_argument("id", help="Entity ID to activate")

    clean_parser = subparsers.add_parser("clean", help="Clear cache")
    archive_parser = subparsers.add_parser("archive", help="Move processed inputs to archive folder")

    # New command: Compact
    compact_parser = subparsers.add_parser("compact", help="Merge all knowledge into a snapshot")

    args = parser.parse_args()

    root = args.root
    if not os.path.exists(root):
        print(f"[!] Error: Brain root '{root}' does not exist.")
        sys.exit(1)

    if args.command == "archive":
        archive_inputs(root)
        sys.exit(0)

    cortex = Cortex(root)
    factory = KnowledgeFactory(root)
    evolver = Evolver(root)

    if args.command == "status":
        cortex.load_graph()
        report = cortex.analyze_entropy()
        print(f"\n🧠 CORTEX STATUS REPORT")
        print(f"Entities: {report.total_nodes} | Relations: {report.total_edges} | Density: {report.density:.4f}")
    elif args.command == "search":
        cortex.load_graph()
        results = cortex.search_concepts(args.query)
        for r in results:
            print(f"  - [{r.id}] {r.name} (Weight: {r.weight:.2f})")
            factory.activate_memory(r.id) # Autonomic activation on search
    elif args.command == "visualize":
        cortex.load_graph()
        print(cortex.export_mermaid())
    elif args.command == "evolve":
        evolver.run_cycle()
    elif args.command == "clean":
        clean_cache(root)
    elif args.command == "connect":
        try:
            factory.add_relation({"src": args.src, "rel": args.rel, "dst": args.dst, "context": args.context, "created_at": datetime.now().isoformat()})
        except ValueError as e: print(f"[!] Error: {e}")
    elif args.command == "add":
        try:
            tags = [t.strip() for t in args.tags.split(",")] if args.tags else []
            factory.add_entity(args.category, {"id": args.id, "type": args.type, "name": args.name, "desc": args.desc, "tags": tags, "updated_at": datetime.now().isoformat()})
        except ValueError as e: print(f"[!] Error: {e}")
    elif args.command == "touch" or args.command == "activate":
        try:
            factory.activate_memory(args.id)
        except ValueError as e: print(f"[!] Error: {e}")
    elif args.command == "compact":
        cortex.load_graph()
        cortex.save_snapshot()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
