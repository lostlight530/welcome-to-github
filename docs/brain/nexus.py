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
    from nexus_mcp import mcp
except ImportError:
    # 允许在没有某些组件的情况下运行基础维护命令
    pass

def main():
    parser = argparse.ArgumentParser(description="NEXUS CORTEX: The Biological Intelligence Engine")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Command: Evolve (The Heartbeat)
    subparsers.add_parser('evolve', help='Run the biological OODA loop (Harvester -> Cortex -> Evolution)')

    # Command: Harvester (Sensory Only)
    subparsers.add_parser('harvest', help='Run strictly the sensory harvester')

    # Command: Clean (Maintenance)
    subparsers.add_parser('clean', help='Remove temporary artifacts (caches, logs)')

    # Command: Visualize
    subparsers.add_parser('visualize', help='Generate Mermaid.js graph of the Cortex')

    # Command: Search
    search_parser = subparsers.add_parser('search', help='Synaptic associative search')
    search_parser.add_argument('query', type=str, help='Search query')

    # Command: Connect (Manual Synapse)
    connect_parser = subparsers.add_parser('connect', help='Manually connect two entities')
    connect_parser.add_argument('source', type=str)
    connect_parser.add_argument('relation', type=str)
    connect_parser.add_argument('target', type=str)
    connect_parser.add_argument('--desc', type=str, default="", help='Description of the connection')

    # Command: Add Entity
    add_parser = subparsers.add_parser('add', help='Add a new entity manually')
    add_parser.add_argument('type', choices=['entity'], help='Object type')
    add_parser.add_argument('--id', required=True)
    add_parser.add_argument('--name', required=True)
    add_parser.add_argument('--type_slug', default='concept')
    add_parser.add_argument('--desc', default='')

    # Command: Activate
    activate_parser = subparsers.add_parser('activate', help='Boost memory weight manually')
    activate_parser.add_argument('id', type=str)

    # Command: Archive
    subparsers.add_parser('archive', help='Move processed inputs to archive')

    # Command: Status
    subparsers.add_parser('status', help='Show db status')

    # Command: Intuition
    subparsers.add_parser('intuition', help='Show subconscious intuitions')

    # Command: Decay
    subparsers.add_parser('decay', help='Force memory decay cycle')

    args = parser.parse_args()

    # --- Execution Logic ---

    base_path = Path(__file__).parent

    if args.command == 'clean':
        print("🧹 Cleaning Cortex environment...")
        targets = [
            base_path / "__pycache__",
            base_path / ".pytest_cache",
            base_path / "inputs" / "__pycache__"
        ]

        # [CRITICAL FIX] Protect the Harvester State
        protected_files = {".harvester_state.json"}

        for t in targets:
            if t.exists() and t.is_dir():
                shutil.rmtree(t)
                print(f"   - Removed {t.name}")
            elif t.exists() and t.is_file():
                os.remove(t)
                print(f"   - Removed {t.name}")

        # 清理 inputs 目录下的临时文件，但避开受保护文件
        inputs_dir = base_path / "inputs"
        if inputs_dir.exists():
            for f in inputs_dir.iterdir():
                if f.name.endswith(".tmp") or f.name == ".DS_Store" or f.name == ".pytest_cache" or f.name == "__pycache__":
                    if f.is_dir():
                        shutil.rmtree(f)
                    else:
                        os.remove(f)
                    print(f"   - Removed garbage: {f.name}")
                elif f.name in protected_files:
                    print(f"   - 🛡️ Protected persistent state: {f.name}")

        print("✨ Environment pristine.")

    elif args.command == 'evolve':
        print("🧬 Starting Evolution Cycle...")
        # 1. Harvest
        h = Harvester(base_path)
        new_data = h.fetch_github_data()

        # 2. Evolve (Decay + Intuition + Mission)
        e = Evolver(base_path)
        e.run_daily_cycle()

    elif args.command == 'harvest':
        h = Harvester(base_path)
        h.fetch_github_data()

    elif args.command == 'search':
        c = Cortex(base_path / "cortex.db")
        results = c.search(args.query)
        print(f"🔍 Synaptic Search Results for '{args.query}':")
        for r in results:
            icon = "🔗" if r.get('distance', 0) > 0 else "🎯"
            print(f" {icon} [{r['weight']:.2f}] {r['name']} ({r['id']}) - {r['desc'][:60]}...")

    elif args.command == 'connect':
        c = Cortex(base_path / "cortex.db")
        c.connect_entities(args.source, args.relation, args.target, args.desc)
        print(f"⚡ Synapse established: {args.source} --[{args.relation}]--> {args.target}")

    elif args.command == 'activate':
        c = Cortex(base_path / "cortex.db")
        c.activate_memory(args.id)
        print(f"🔥 Memory activated: {args.id}")

    elif args.command == 'archive':
        e = Evolver(base_path)
        e.archive_inputs()

    elif args.command == 'add':
        c = Cortex(base_path / "cortex.db")
        if getattr(args, 'type', None) == 'entity':
            c.add_entity(args.id, args.type_slug, args.name, args.desc)
            print(f"🌱 Entity created: {args.name}")

    elif args.command == 'status':
        c = Cortex(base_path / "cortex.db")
        stats = c.get_stats()
        print(f"🧠 CORTEX STATUS: Entities: {stats['entities']} | Relations: {stats['relations']} | Density: {stats['density']:.4f}")

    elif args.command == 'intuition':
        e = Evolver(base_path)
        ints = e._incubate_ideas()
        if not ints:
            print("💤 No intuitions currently.")
        else:
            print("\n".join(ints))

    elif args.command == 'decay':
        c = Cortex(base_path / "cortex.db")
        c.decay_memories()
        print("📉 Memories decayed.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
