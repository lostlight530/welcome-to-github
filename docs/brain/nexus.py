#!/usr/bin/env python3
import argparse
import sys
import os
import json
from datetime import datetime

# Add current directory to path so imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cortex import Cortex
from factory import KnowledgeFactory
from evolution import Evolver

def main():
    parser = argparse.ArgumentParser(description="NEXUS CORTEX: Cognitive Synthesis Protocol CLI")
    parser.add_argument("--root", default="docs/brain", help="Path to brain root directory")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 1. Status
    status_parser = subparsers.add_parser("status", help="Show cognitive entropy report")

    # 2. Search
    search_parser = subparsers.add_parser("search", help="Search for concepts")
    search_parser.add_argument("query", help="Search term")

    # 3. Visualize
    viz_parser = subparsers.add_parser("visualize", help="Generate Mermaid.js graph")

    # 4. Evolve
    evolve_parser = subparsers.add_parser("evolve", help="Run the OODA evolution cycle")

    # 5. Connect (Quick Relation)
    connect_parser = subparsers.add_parser("connect", help="Connect two concepts")
    connect_parser.add_argument("src", help="Source Entity ID")
    connect_parser.add_argument("rel", help="Relation (e.g. 'uses', 'is_a')")
    connect_parser.add_argument("dst", help="Destination Entity ID")
    connect_parser.add_argument("--context", default="", help="Context/Source for this connection")

    # 6. Add Entity
    add_parser = subparsers.add_parser("add", help="Add a new entity")
    add_parser.add_argument("category", help="Category/File (e.g. 'concepts', 'tech_stack')")
    add_parser.add_argument("--id", required=True, help="Unique ID slug")
    add_parser.add_argument("--type", required=True, help="Type (concept, tech, person)")
    add_parser.add_argument("--name", required=True, help="Human readable name")
    add_parser.add_argument("--desc", required=True, help="Description")
    add_parser.add_argument("--tags", help="Comma-separated tags")

    args = parser.parse_args()

    # Initialize Core Components
    root = args.root
    if not os.path.exists(root):
        print(f"[!] Error: Brain root '{root}' does not exist.")
        sys.exit(1)

    cortex = Cortex(root)
    factory = KnowledgeFactory(root)
    evolver = Evolver(root)

    if args.command == "status":
        cortex.load_graph()
        report = cortex.analyze_entropy()
        print(f"\n🧠 CORTEX STATUS REPORT")
        print(f"========================")
        print(f"Entities:    {report.total_nodes}")
        print(f"Relations:   {report.total_edges}")
        print(f"Density:     {report.density:.4f}")
        print(f"Orphans:     {len(report.orphan_nodes)}")
        print(f"Stale:       {len(report.stale_nodes)}")
        if report.broken_links:
            print(f"\n[!] BROKEN LINKS DETECTED: {len(report.broken_links)}")
            for err in report.broken_links:
                print(f"  - {err}")
            sys.exit(1)

    elif args.command == "search":
        cortex.load_graph()
        results = cortex.search_concepts(args.query)
        print(f"\n🔎 Search Results for '{args.query}':")
        for r in results:
            print(f"  - [{r.id}] {r.name}: {r.desc[:50]}...")

    elif args.command == "visualize":
        cortex.load_graph()
        print(cortex.export_mermaid())

    elif args.command == "evolve":
        evolver.run_cycle()

    elif args.command == "connect":
        try:
            factory.add_relation({
                "src": args.src,
                "rel": args.rel,
                "dst": args.dst,
                "context": args.context,
                "created_at": datetime.now().isoformat()
            })
        except ValueError as e:
            print(f"[!] Error: {e}")
            sys.exit(1)

    elif args.command == "add":
        tags = args.tags.split(",") if args.tags else []
        data = {
            "id": args.id,
            "type": args.type,
            "name": args.name,
            "desc": args.desc,
            "tags": [t.strip() for t in tags],
            "updated_at": datetime.now().isoformat()
        }
        try:
            factory.add_entity(args.category, data)
        except ValueError as e:
            print(f"[!] Error: {e}")
            sys.exit(1)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
