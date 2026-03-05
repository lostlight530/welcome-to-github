import argparse
import os
from cortex import Cortex, Entity, Relation
from evolution import Evolver

def main():
    parser = argparse.ArgumentParser(description="NEXUS CORTEX CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Command: add
    add_parser = subparsers.add_parser("add", help="Add knowledge")
    add_sub = add_parser.add_subparsers(dest="object")

    ent_parser = add_sub.add_parser("entity")
    ent_parser.add_argument("--id", required=True)
    ent_parser.add_argument("--type", required=True)
    ent_parser.add_argument("--name", required=True)
    ent_parser.add_argument("--desc", default="")

    # Command: connect
    conn_parser = subparsers.add_parser("connect", help="Connect entities")
    conn_parser.add_argument("source")
    conn_parser.add_argument("relation")
    conn_parser.add_argument("target")
    conn_parser.add_argument("--desc", default="")

    # Command: search
    search_parser = subparsers.add_parser("search", help="Search knowledge")
    search_parser.add_argument("query")

    # Command: evolve (Runs OODA)
    subparsers.add_parser("evolve", help="Run OODA Loop")

    # Command: archive (Clean inputs)
    subparsers.add_parser("archive", help="Archive processed inputs")

    # Command: decay (Manual Forgetting)
    subparsers.add_parser("decay", help="Force memory decay cycle")

    # Command: intuition (Show guesses)
    subparsers.add_parser("intuition", help="Show subconscious intuitions")

    # Command: activate
    activate_parser = subparsers.add_parser("activate", help="Activate memory")
    activate_parser.add_argument("id")

    # Status
    subparsers.add_parser("status", help="Show db status")

    args = parser.parse_args()

    # In GitHub Actions, ensure the directory exists
    os.makedirs("docs/brain", exist_ok=True)
    cortex = Cortex("docs/brain/cortex.db")

    if args.command == "add":
        if args.object == "entity":
            e = Entity(id=args.id, type=args.type, name=args.name, desc=args.desc)
            cortex.add_entity(e)
            print(f"✅ Entity added: {args.name}")

    elif args.command == "connect":
        r = Relation(source=args.source, relation=args.relation, target=args.target, annotation=args.desc)
        cortex.add_relation(r)
        print(f"🔗 Connected: {args.source} --[{args.relation}]--> {args.target}")

    elif args.command == "search":
        results = cortex.search(args.query)
        print(f"🔍 Found {len(results)} results:")
        for r in results:
            print(f"  - [{r['id']}] {r['name']} (Weight: {r.get('weight', 1.0):.2f})")
            print(f"    {r['desc'][:60]}...")

    elif args.command == "evolve":
        evolver = Evolver(cortex)
        evolver.run_daily_cycle()
        print("🧬 Evolution cycle complete.")

    elif args.command == "decay":
        cortex.decay_memories()
        print("📉 Memories decayed.")

    elif args.command == "activate":
        cortex.activate_memory(args.id)
        print(f"⚡ Memory {args.id} activated.")

    elif args.command == "intuition":
        evolver = Evolver(cortex)
        ints = evolver._incubate_ideas()
        if not ints:
            print("💤 No intuitions currently.")
        else:
            print("\n".join(ints))

    elif args.command == "archive":
        import shutil
        base = "docs/brain/inputs"
        archive_base = "docs/brain/inputs/archive"
        count = 0
        if os.path.exists(base):
            for root, _, files in os.walk(base):
                if "archive" in root: continue
                for f in files:
                    if f.endswith(".md") and not f.startswith("."):
                        src = os.path.join(root, f)
                        rel = os.path.relpath(src, base)
                        dst = os.path.join(archive_base, rel)
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        shutil.move(src, dst)
                        count += 1
        print(f"📦 Archived {count} files.")

    elif args.command == "status":
        cursor = cortex.conn.cursor()
        e_count = cursor.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
        r_count = cursor.execute("SELECT COUNT(*) FROM relations").fetchone()[0]
        print(f"🧠 CORTEX STATUS: Entities: {e_count} | Relations: {r_count}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()