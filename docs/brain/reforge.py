import sys
import os
import json
from datetime import datetime

# Ensure we can import factory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from factory import KnowledgeFactory

def reforge(root_dir):
    f = KnowledgeFactory(root_dir)
    print("[Reforge] Injecting 2026 Q1 Edge AI Landscape...")

    # Data from User (High Quality)
    data = [
        {"id": "mediapipe", "type": "tech", "name": "MediaPipe", "desc": "Google's on-device ML framework.", "tags": ["google", "edge-ai"]},
        {"id": "npu", "type": "tech", "name": "NPU", "desc": "Neural Processing Unit.", "tags": ["hardware", "acceleration"]},
        {"id": "jax", "type": "tech", "name": "JAX", "desc": "High-performance numerical computing.", "tags": ["google", "research"]},
        {"id": "mindspore", "type": "tech", "name": "MindSpore", "desc": "Huawei's AI framework.", "tags": ["huawei", "edge-ai"]},
        {"id": "mcp", "type": "protocol", "name": "MCP", "desc": "Model Context Protocol.", "tags": ["standard", "agent"]},
        {"id": "dify", "type": "tool", "name": "Dify", "desc": "LLM App Development Platform.", "tags": ["low-code", "agent"]},
        {"id": "vllm", "type": "tech", "name": "vLLM", "desc": "High-throughput inference engine.", "tags": ["inference", "server"]},
        {"id": "ollama", "type": "tool", "name": "Ollama", "desc": "Get up and running with Llama 3.", "tags": ["local-llm", "tool"]},
        {"id": "open-webui", "type": "tool", "name": "Open WebUI", "desc": "User-friendly AI Interface.", "tags": ["ui", "python"]},
    ]

    relations = [
        ("mediapipe", "supports", "npu", "v0.10.33 Release Note"),
        ("mindspore", "optimizes", "transformer", "Recent Commits"),
        ("jax", "deprecates", "legacy-xla", "v0.9.1 Breaking Change"),
        ("mcp", "expands_to", "database-servers", "Release 2026.2.25"),
        ("dify", "enables", "agentic-workflow", "Ecosystem Consensus"),
        ("ollama", "supports", "deepseek", "v0.17.0 Release"),
        ("open-webui", "interacts_with", "ollama", "Integration Docs"),
    ]

    # Ingest Entities
    for item in data:
        try:
            f.add_entity("tech_stack" if item['type'] == 'tech' else "concepts", {
                "id": item['id'],
                "type": item['type'],
                "name": item['name'],
                "desc": item['desc'],
                "tags": item['tags'],
                "updated_at": datetime.now().isoformat()
            })
        except Exception as e:
            print(f"Error adding {item['id']}: {e}")

    # Ingest Relations
    for src, rel, dst, ctx in relations:
        try:
            # Auto-create dst if missing (lazy fix for this script)
            if dst not in f.cortex.entities:
                f.add_entity("concepts", {"id": dst, "type": "concept", "name": dst.title(), "desc": "Auto-generated concept", "tags": ["auto"]})

            f.add_relation({
                "src": src, "rel": rel, "dst": dst, "context": ctx, "created_at": datetime.now().isoformat()
            })
        except Exception as e:
            print(f"Error connecting {src}->{dst}: {e}")

if __name__ == "__main__":
    reforge("docs/brain")
