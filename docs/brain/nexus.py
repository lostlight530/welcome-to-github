# [FILE: docs/brain/nexus.py]
import sys
import os
import argparse
import shutil
import json
from pathlib import Path

# Try imports
try:
    from cortex import Cortex
    from harvester import Harvester
    from evolution import Evolver
    from scholar import Scholar
except ImportError:
    pass

def main():
    parser = argparse.ArgumentParser(description="NEXUS CORTEX: The Sovereign Intelligence")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Commands
    subparsers.add_parser('evolve', help='Run Daily Cycle')
    subparsers.add_parser('harvest', help='Run Harvester')
    subparsers.add_parser('rebuild', help='Rebuild DB from Text (The Restoration)')

    learn_parser = subparsers.add_parser('learn', help='Ingest Knowledge')
    learn_parser.add_argument('file', help='Path to file')

    subparsers.add_parser('clean', help='Cleanup')
    subparsers.add_parser('status', help='Show db status')

    # Synapse Ops
    search_parser = subparsers.add_parser('search', help='Search Memory')
    search_parser.add_argument('query', type=str)

    connect_parser = subparsers.add_parser('connect', help='Create Connection')
    connect_parser.add_argument('source', type=str)
    connect_parser.add_argument('relation', type=str)
    connect_parser.add_argument('target', type=str)
    connect_parser.add_argument('--desc', type=str, default="")

    add_parser = subparsers.add_parser('add', help='Create Entity')
    add_parser.add_argument('type', choices=['entity'], help='Type')
    add_parser.add_argument('--id', required=True)
    add_parser.add_argument('--name', required=True)
    add_parser.add_argument('--type_slug', default='concept')
    add_parser.add_argument('--desc', default='')

    activate_parser = subparsers.add_parser('activate', help='Boost Weight')
    activate_parser.add_argument('id', type=str)

    args = parser.parse_args()
    base_path = Path(__file__).parent

    # --- Logic ---

    if args.command == 'clean':
        print("🧹 Cleaning Cortex...")
        targets = [base_path / "__pycache__", base_path / ".pytest_cache", base_path / "inputs" / "__pycache__"]
        for t in targets:
            if t.exists(): shutil.rmtree(t)

        # Protected Cleanup
        inputs_dir = base_path / "inputs"
        protected = {".harvester_state.json", ".gitkeep"}
        if inputs_dir.exists():
            for f in inputs_dir.iterdir():
                if f.is_file() and f.name not in protected and (f.name.endswith(".tmp") or f.name == ".DS_Store"):
                    os.remove(f)
        print("✨ Cleaned.")

    elif args.command == 'rebuild':
        print("🧠 Initiating Cortex Reconstruction Protocol...")
        # Force a fresh DB connection implicitly creates it
        c = Cortex(base_path / "cortex.db")
        knowledge_dir = base_path / "knowledge"

        count = 0
        for root, _, files in os.walk(knowledge_dir):
            for file in files:
                if file.endswith(".jsonl"):
                    filepath = Path(root) / file
                    print(f"   - Ingesting: {file}...")
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            for line in f:
                                if not line.strip(): continue
                                data = json.loads(line)
                                if 'src' in data: # Relation
                                    c.connect_entities(data['src'], data.get('relation', data.get('rel', 'connected')), data['dst'], data.get('desc',''))
                                else: # Entity
                                    c.add_entity(data.get('id'), data.get('type', 'concept'), data.get('name'), data.get('desc',''))
                                count += 1
                    except Exception as e:
                        print(f"     ⚠️ Error in {file}: {e}")
        print(f"✨ Reconstruction Complete. {count} memories restored.")

    elif args.command == 'evolve':
        h = Harvester(base_path)
        h.fetch_github_data()
        e = Evolver(base_path)
        e.run_daily_cycle()

    elif args.command == 'harvest':
        h = Harvester(base_path)
        h.fetch_github_data()

    elif args.command == 'learn':
        s = Scholar(base_path)
        print(f"🎓 Record: {s.learn(args.file)}")

    elif args.command == 'search':
        c = Cortex(base_path / "cortex.db")
        for r in c.search(args.query):
            icon = "🔗" if r.get('distance', 0) > 0 else "🎯"
            print(f" {icon} [{r['weight']:.2f}] {r['name']} ({r['id']})")

    elif args.command == 'connect':
        c = Cortex(base_path / "cortex.db")
        c.connect_entities(args.source, args.relation, args.target, args.desc)
        print("⚡ Connected.")

    elif args.command == 'add':
        c = Cortex(base_path / "cortex.db")
        c.add_entity(args.id, args.type_slug, args.name, args.desc)
        print("🌱 Created.")

    elif args.command == 'activate':
        c = Cortex(base_path / "cortex.db")
        c.activate_memory(args.id)
        print("🔥 Activated.")

    elif args.command == 'status':
        c = Cortex(base_path / "cortex.db")
        stats = c.get_stats()
        print(f"📊 Cortex Status:")
        print(f"   - Entities: {stats['entities']}")
        print(f"   - Relations: {stats['relations']}")
        print(f"   - Network Density (avg weight): {stats['density']:.4f}")

    elif args.command == 'rebuild':
        import json
        print("🧠 Initiating Cortex Reconstruction Protocol...")
        c = Cortex(base_path / "cortex.db")
        knowledge_dir = base_path / "knowledge"

        count = 0
        # 遍历 knowledge 目录下的所有 jsonl 文件
        for root, dirs, files in os.walk(knowledge_dir):
            for file in files:
                if file.endswith(".jsonl"):
                    filepath = Path(root) / file
                    print(f"   - Ingesting: {file}...")
                    with open(filepath, 'r', encoding='utf-8') as f:
                        for line in f:
                            try:
                                data = json.loads(line)
                                # 区分实体和关系（根据文件路径或数据结构）
                                if 'src' in data and 'dst' in data:
                                    # 这是一个关系
                                    c.connect_entities(
                                        data['src'],
                                        data.get('rel', data.get('relation', 'connected_to')),
                                        data['dst']
                                    )
                                else:
                                    # 这是一个实体
                                    c.add_entity(
                                        id=data.get('id'),
                                        type_slug=data.get('type', 'concept'),
                                        name=data.get('name'),
                                        desc=data.get('desc', '')
                                    )
                                count += 1
                            except Exception as e:
                                print(f"     ⚠️ Error parsing line: {e}")

        print(f"✨ Reconstruction Complete. {count} memories restored.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()