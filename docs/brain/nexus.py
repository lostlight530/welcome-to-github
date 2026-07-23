import datetime
import sys
import traceback
import os
import argparse
import shutil
import json
from pathlib import Path

# Lazy Imports
try:
    from cortex import Cortex
    from harvester import Harvester
    from evolution import Evolver
    from scholar import Scholar
    from reason import ReasoningEngine # <--- The Frontal Lobe
    from factory import KnowledgeFactory
except ImportError:
    pass

BRAIN_ROOT = Path(__file__).parent
DB_PATH = BRAIN_ROOT / "cortex.db"

def main() -> None:
    cortex = None
    factory = None
    try:
        parser = argparse.ArgumentParser(description="NEXUS CORTEX: The Sovereign Intelligence")
        subparsers = parser.add_subparsers(dest='command', help='Available commands')

        # --- Life Cycle ---
        subparsers.add_parser('evolve', help='Run Daily Cycle (Harvest -> Dream -> Plan)')
        subparsers.add_parser('harvest', help='Run Sensory Harvester (External)')
        subparsers.add_parser('project', help='Project current external evidence into the graph')
        subparsers.add_parser('ingest', help='Deep Scan Codebase (Internal)') # <--- Omniscience
        subparsers.add_parser('ponder', help='Run Deep Inference (Cognition)') # <--- Reasoning
        subparsers.add_parser('rebuild', help='Rebuild DB from Text (Restoration)')
        subparsers.add_parser('clean', help='Cleanup environment')

        # --- Data Entry ---
        add_parser = subparsers.add_parser('add', help='Add a new knowledge entity')
        add_parser.add_argument('category', type=str, help='Category (e.g., concepts, tech_stack)')
        add_parser.add_argument('id', type=str, help='Unique ID (e.g., semantic_kernel)')
        add_parser.add_argument('type', type=str, help='Entity Type')
        add_parser.add_argument('name', type=str, help='Human readable name')
        add_parser.add_argument('desc', type=str, help='Short description')

        connect_parser = subparsers.add_parser('connect', help='Connect two entities')
        connect_parser.add_argument('src', type=str)
        connect_parser.add_argument('rel', type=str)
        connect_parser.add_argument('dst', type=str)
        connect_parser.add_argument('--desc', type=str, default="", help='Context for the relation')

        # --- Retrieval ---
        search_parser = subparsers.add_parser('search', help='Search Knowledge Graph')
        search_parser.add_argument('query', type=str, help='Keyword to search')

        subparsers.add_parser('status', help='View Brain Entropy & Stats')

        args = parser.parse_args()

        if not args.command:
            parser.print_help()
            sys.exit(1)

        cortex = Cortex(DB_PATH)

        if args.command == 'evolve':
            from evolution import Evolver
            evolver = Evolver(BRAIN_ROOT)
            evolver.run_daily_cycle()

        elif args.command == 'harvest':
            from harvester import Harvester
            h = Harvester(BRAIN_ROOT)
            h.fetch_github_data()

        elif args.command == 'project':
            from document_hygiene import project_current_snapshots
            print(project_current_snapshots(BRAIN_ROOT / "inputs", BRAIN_ROOT / "knowledge"))

        elif args.command == 'ingest':
            from scholar import Scholar
            s = Scholar(BRAIN_ROOT)
            s.ingest_repository(BRAIN_ROOT.parent.parent)

        elif args.command == 'ponder':
            from reason import ReasoningEngine
            r = ReasoningEngine(BRAIN_ROOT)
            insights = r.ponder()
            print("\\n[NEXUS] 🧠 Deep Inference Results:")
            for insight in insights:
                print(f"  - {insight}")

        elif args.command == 'rebuild':
            cortex.conn.close()
            cortex = None
            if DB_PATH.exists():
                os.remove(DB_PATH)
            cortex = Cortex(DB_PATH)

            import glob
            # Load entities
            print("Rebuilding entities... / 正在重建实体...")
            for f_path in glob.glob(str(BRAIN_ROOT / "knowledge" / "entities" / "*.jsonl"), recursive=True):
                with open(f_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        try:
                            data = json.loads(line)
                            if 'id' in data and 'type' in data and 'name' in data and 'desc' in data:
                                cortex.add_entity(data['id'], data['type'], data['name'], data['desc'], save_to_disk=False)
                        except:
                            pass

            # Load relations
            print("Rebuilding relations... / 正在重建关系...")
            for f_path in glob.glob(str(BRAIN_ROOT / "knowledge" / "relations" / "*.jsonl"), recursive=True):
                with open(f_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        try:
                            data = json.loads(line)
                            # Sometimes relations have 'rel' instead of 'relation' in older JSONLs, let's support both
                            rel = data.get('relation') or data.get('rel')
                            if 'src' in data and rel and 'dst' in data:
                                cortex.connect_entities(data['src'], rel, data['dst'], data.get('desc', data.get('context', '')), save_to_disk=False)
                        except:
                            pass

            print("Database rebuilt from schemas and JSONL fragments. / 数据库已从 Schema 和 JSONL 碎片重建。")

        elif args.command == 'clean':
            cortex.conn.close()
            cortex = None
            # Safe cleanup, protect `.harvester_state.json`
            if DB_PATH.exists(): os.remove(DB_PATH)
            if DB_PATH.with_suffix('.db-journal').exists(): os.remove(DB_PATH.with_suffix('.db-journal'))
            print("Temporary caches cleared. / 临时缓存已清理。")

        elif args.command == 'add':
            factory = KnowledgeFactory(str(BRAIN_ROOT))
            data = {"id": args.id, "type": args.type, "name": args.name, "desc": args.desc, "updated_at": datetime.datetime.now().isoformat(), "tags": []}
            factory.add_entity(args.category, data)

        elif args.command == 'connect':
            factory = KnowledgeFactory(str(BRAIN_ROOT))
            data = {"src": args.src, "rel": args.rel, "dst": args.dst, "context": args.desc, "created_at": datetime.datetime.now().isoformat()}
            factory.add_relation(data)

        elif args.command == 'search':
            results = cortex.search(args.query)
            for res in results:
                print(f"[{res['distance']}] {res['name']} ({res['id']}): {res['desc'][:50]}...")

        elif args.command == 'status':
            stats = cortex.get_stats()
            print("🧠 NEXUS CORTEX STATUS / 状态报告")
            print(f"Entities : {stats['entities']}")
            print(f"Relations: {stats['relations']}")
            print(f"Density  : {stats['density']:.4f}")

    except Exception as e:
        traceback.print_exc()
        print(f"[Nexus Error | Nexus 错误] Execution failed / 执行失败: {e}")
        sys.exit(1)
    finally:
        if cortex is not None:
            cortex.conn.close()
        if factory is not None:
            factory.cortex.conn.close()

if __name__ == "__main__":
    main()
