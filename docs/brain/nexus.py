import sys
import os
import argparse
import shutil
from pathlib import Path

# 导入核心组件
try:
    from cortex import Cortex
    from harvester import Harvester
    from evolution import Evolver
    from scholar import Scholar
    from nexus_mcp import mcp
except ImportError:
    pass

def main():
    parser = argparse.ArgumentParser(description="NEXUS CORTEX: The Biological Intelligence Engine")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # --- Core Commands ---
    subparsers.add_parser('evolve', help='Run the daily OODA loop (Harvest -> Dream -> Plan)')
    subparsers.add_parser('harvest', help='Run strictly the sensory harvester')

    # Command: Learn (Ingest Knowledge)
    learn_parser = subparsers.add_parser('learn', help='Ingest a file into long-term memory')
    learn_parser.add_argument('file', help='Path to document')

    # Command: Clean (Maintenance)
    subparsers.add_parser('clean', help='Remove temporary artifacts (caches, logs)')

    # --- Synaptic Commands ---
    search_parser = subparsers.add_parser('search', help='Synaptic associative search')
    search_parser.add_argument('query', type=str, help='Search query')

    connect_parser = subparsers.add_parser('connect', help='Manually connect two entities')
    connect_parser.add_argument('source', type=str)
    connect_parser.add_argument('relation', type=str)
    connect_parser.add_argument('target', type=str)
    connect_parser.add_argument('--desc', type=str, default="", help='Description')

    add_parser = subparsers.add_parser('add', help='Add a new entity manually')
    add_parser.add_argument('type', choices=['entity'], help='Object type')
    add_parser.add_argument('--id', required=True)
    add_parser.add_argument('--name', required=True)
    add_parser.add_argument('--type_slug', default='concept')
    add_parser.add_argument('--desc', default='')

    activate_parser = subparsers.add_parser('activate', help='Boost memory weight manually')
    activate_parser.add_argument('id', type=str)

    args = parser.parse_args()
    base_path = Path(__file__).parent

    # --- Execution Logic ---

    if args.command == 'clean':
        print("🧹 Cleaning Cortex environment...")
        # 1. Python Cache
        targets = [
            base_path / "__pycache__",
            base_path / ".pytest_cache",
            base_path / "inputs" / "__pycache__"
        ]
        for t in targets:
            if t.exists():
                shutil.rmtree(t)
                print(f"   - Removed {t.name}")

        # 2. Input Temp Files (CRITICAL: Protect State)
        inputs_dir = base_path / "inputs"
        protected_files = {".harvester_state.json", ".gitkeep"}

        if inputs_dir.exists():
            for f in inputs_dir.iterdir():
                if f.is_file() and f.name not in protected_files:
                    if f.name.endswith(".tmp") or f.name == ".DS_Store":
                        os.remove(f)
                        print(f"   - Removed garbage: {f.name}")
                    # Note: We do NOT delete .md files here anymore to allow 'evolve' to process them.
                    # Only 'archive' command moves them.

        print("✨ Environment pristine. Radar state preserved.")

    elif args.command == 'evolve':
        print("🧬 Starting Evolution Cycle...")
        # 1. Harvest
        h = Harvester(base_path)
        h.fetch_github_data()
        # 2. Evolve
        e = Evolver(base_path)
        e.run_daily_cycle()

    elif args.command == 'harvest':
        h = Harvester(base_path)
        h.fetch_github_data()

    elif args.command == 'learn':
        s = Scholar(base_path)
        rec = s.learn(args.file)
        if rec: print(f"🎓 Learned: {rec}")
        else: print("❌ File not found or empty.")

    elif args.command == 'search':
        c = Cortex(base_path / "cortex.db")
        results = c.search(args.query)
        print(f"🔍 Synaptic Search Results for '{args.query}':")
        for r in results:
            icon = "🔗" if r.get('distance', 0) > 0 else "🎯"
            print(f" {icon} [{r['weight']:.2f}] {r['name']} ({r['id']})")
            print(f"    {r['desc'][:80]}...")

    elif args.command == 'connect':
        c = Cortex(base_path / "cortex.db")
        c.connect_entities(args.source, args.relation, args.target, args.desc)
        print(f"⚡ Synapse: {args.source} --[{args.relation}]--> {args.target}")

    elif args.command == 'activate':
        c = Cortex(base_path / "cortex.db")
        c.activate_memory(args.id)
        print(f"🔥 Activated: {args.id}")

    elif args.command == 'add':
        c = Cortex(base_path / "cortex.db")
        c.add_entity(args.id, args.type_slug, args.name, args.desc)
        print(f"🌱 Created: {args.name}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
