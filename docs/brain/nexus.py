#!/usr/bin/env python3
import argparse
import sys
import os
import shutil
import glob
from datetime import datetime

# Add current directory to path so imports work
# 将当前目录添加到路径，以便导入工作
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cortex import Cortex
from factory import KnowledgeFactory
from evolution import Evolver
from learner import DeterministicScholar

def clean_cache(root_dir: str):
    """
    Cleans __pycache__ and temporary files.
    清除 __pycache__ 和临时文件。
    """
    print(f"[Nexus] Cleaning cache in {root_dir}...")

    # 1. Remove __pycache__ directories
    # 1. 删除 __pycache__ 目录
    for pycache in glob.glob(os.path.join(root_dir, "**", "__pycache__"), recursive=True):
        try:
            shutil.rmtree(pycache)
            print(f"  - Removed: {pycache}")
        except Exception as e:
            print(f"  ! Failed to remove {pycache}: {e}")

    # 2. Remove .cache or temp files if any (future proofing)
    # 2. 删除 .cache 或临时文件（如果有，为未来做准备）
    temp_patterns = ["*.pyc", "*.tmp", ".DS_Store"]
    for pattern in temp_patterns:
        for temp_file in glob.glob(os.path.join(root_dir, "**", pattern), recursive=True):
            try:
                os.remove(temp_file)
                print(f"  - Removed: {temp_file}")
            except Exception as e:
                print(f"  ! Failed to remove {temp_file}: {e}")

    print("[Nexus] Cache clean complete. (缓存清理完成)")

def main():
    parser = argparse.ArgumentParser(description="NEXUS CORTEX: Cognitive Synthesis Protocol CLI (认知合成协议命令行接口)")
    parser.add_argument("--root", default="docs/brain", help="Path to brain root directory (大脑根目录路径)")

    subparsers = parser.add_subparsers(dest="command", help="Available commands (可用命令)")

    # 1. Status
    status_parser = subparsers.add_parser("status", help="Show cognitive entropy report (显示认知熵报告)")

    # 2. Search
    search_parser = subparsers.add_parser("search", help="Search for concepts (搜索概念)")
    search_parser.add_argument("query", help="Search term (搜索词)")

    # 3. Visualize
    viz_parser = subparsers.add_parser("visualize", help="Generate Mermaid.js graph (生成 Mermaid.js 图谱)")

    # 4. Evolve
    evolve_parser = subparsers.add_parser("evolve", help="Run the OODA evolution cycle (运行 OODA 进化循环)")

    # 5. Connect (Quick Relation)
    connect_parser = subparsers.add_parser("connect", help="Connect two concepts (连接两个概念)")
    connect_parser.add_argument("src", help="Source Entity ID (源实体 ID)")
    connect_parser.add_argument("rel", help="Relation (e.g. 'uses', 'is_a') (关系，如 'uses')")
    connect_parser.add_argument("dst", help="Destination Entity ID (目标实体 ID)")
    connect_parser.add_argument("--context", default="", help="Context/Source for this connection (上下文/来源)")

    # 6. Add Entity
    add_parser = subparsers.add_parser("add", help="Add a new entity (添加新实体)")
    add_parser.add_argument("category", help="Category/File (e.g. 'concepts', 'tech_stack') (类别/文件名)")
    add_parser.add_argument("--id", required=True, help="Unique ID slug (唯一标识符)")
    add_parser.add_argument("--type", required=True, help="Type (concept, tech, person) (类型)")
    add_parser.add_argument("--name", required=True, help="Human readable name (名称)")
    add_parser.add_argument("--desc", required=True, help="Description (描述)")
    add_parser.add_argument("--tags", help="Comma-separated tags (标签，逗号分隔)")

    # 7. Clean
    clean_parser = subparsers.add_parser("clean", help="Clear cache and temporary files (清除缓存和临时文件)")

    # 8. Learn
    learn_parser = subparsers.add_parser("learn", help="Trigger specific learning task (触发特定学习任务)")
    learn_parser.add_argument("topic", help="Topic key (e.g. 'Anthropic-MCP')")

    args = parser.parse_args()

    # Initialize Core Components
    # 初始化核心组件
    root = args.root
    if not os.path.exists(root):
        print(f"[!] Error: Brain root '{root}' does not exist. (错误：大脑根目录 '{root}' 不存在。)")
        sys.exit(1)

    cortex = Cortex(root)
    factory = KnowledgeFactory(root)
    evolver = Evolver(root)

    if args.command == "status":
        cortex.load_graph()
        report = cortex.analyze_entropy()
        print(f"\n🧠 CORTEX STATUS REPORT (大脑状态报告)")
        print(f"========================")
        print(f"Entities (实体):    {report.total_nodes}")
        print(f"Relations (关系):   {report.total_edges}")
        print(f"Density (密度):     {report.density:.4f}")
        print(f"Orphans (孤岛):     {len(report.orphan_nodes)}")
        print(f"Stale (陈旧):       {len(report.stale_nodes)}")
        if report.broken_links:
            print(f"\n[!] BROKEN LINKS DETECTED (检测到断链): {len(report.broken_links)}")
            for err in report.broken_links:
                print(f"  - {err}")
            sys.exit(1)

    elif args.command == "search":
        cortex.load_graph()
        results = cortex.search_concepts(args.query)
        print(f"\n🔎 Search Results for '{args.query}' (搜索结果):")
        for r in results:
            print(f"  - [{r.id}] {r.name}: {r.desc[:50]}...")

    elif args.command == "visualize":
        cortex.load_graph()
        print(cortex.export_mermaid())

    elif args.command == "evolve":
        evolver.run_cycle()

    elif args.command == "clean":
        clean_cache(root)

    elif args.command == "learn":
        scholar = DeterministicScholar(root)
        scholar.run_daily_contemplation(manual_topic=args.topic)

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
