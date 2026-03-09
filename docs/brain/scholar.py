import os
import ast
import re
import datetime
import json
from pathlib import Path

# Try to connect to the Mind
try:
    from cortex import Cortex
except ImportError:
    pass

class Scholar:
    def __init__(self, brain_path):
        self.brain_path = Path(brain_path)
        self.memories_path = self.brain_path / "memories"
        self.db_path = self.brain_path / "cortex.db"
        self.config_path = self.brain_path / "brain_config.json"

        # Connect to Cortex (The Mind)
        self.cortex = Cortex(self.db_path) if self.db_path.parent.exists() else None

        # Load Config (For future personalization)
        self.config = self._load_config()

        # Ignored patterns (Noise Filter)
        self.ignore_dirs = {
            '.git', '__pycache__', 'node_modules', 'cortex.db', 'memories',
            'inputs', 'archaeology', 'venv', '.idea', '.vscode', 'site-packages'
        }
        self.ignore_files = {
            '.DS_Store', 'cortex.db', 'cortex.db-journal', '.gitignore',
            'package-lock.json', 'yarn.lock', 'requirements.txt'
        }

    def _load_config(self):
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f: return json.load(f)
            except: pass
        return {}

    def ingest_repository(self, root_path):
        """[Omniscience Protocol] Deep scan of the codebase."""
        print(f"🧠 Scholar starting deep scan of: {root_path}")
        root = Path(root_path)
        count = 0

        for dirpath, dirnames, filenames in os.walk(root):
            # Prune ignored directories
            dirnames[:] = [d for d in dirnames if d not in self.ignore_dirs]

            for file in filenames:
                if file in self.ignore_files or file.endswith(('.pyc', '.db')): continue

                filepath = Path(dirpath) / file
                try:
                    self._digest_file(root, filepath)
                    count += 1
                except Exception as e:
                    print(f"   ⚠️ Failed to digest {file}: {e}")

        print(f"✅ Ingestion Complete. {count} files mapped into Cortex.")

    def _digest_file(self, root, filepath):
        rel_path = filepath.relative_to(root)
        file_id = f"file_{str(rel_path).replace('/', '_').replace('.', '_')}"

        # 1. Register File Node
        if self.cortex:
            self.cortex.add_entity(
                id=file_id,
                type_slug="code_file",
                name=filepath.name,
                desc=f"Source file at: {rel_path}",
                save_to_disk=True
            )

        # 2. Deep Content Analysis
        if filepath.suffix == '.py':
            self._analyze_python_ast(filepath, file_id)
        elif filepath.suffix == '.md':
            self._analyze_markdown_structure(filepath, file_id)

    def _analyze_python_ast(self, filepath, file_id):
        """Use Python's native AST to understand code structure."""
        if not self.cortex: return
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            tree = ast.parse(content)

            for node in ast.walk(tree):
                # Classes
                if isinstance(node, ast.ClassDef):
                    class_id = f"class_{node.name}"
                    desc = ast.get_docstring(node) or "Python Class"
                    self.cortex.add_entity(class_id, "code_class", node.name, desc[:100], save_to_disk=True)
                    self.cortex.connect_entities(file_id, "defines", class_id, save_to_disk=True)
                    # Inheritance
                    for base in node.bases:
                        if isinstance(base, ast.Name):
                            self.cortex.connect_entities(class_id, "inherits_from", f"class_{base.id}", save_to_disk=True)

                # Functions
                elif isinstance(node, ast.FunctionDef):
                    func_id = f"func_{node.name}"
                    desc = ast.get_docstring(node) or "Python Function"
                    self.cortex.add_entity(func_id, "code_function", node.name, desc[:100], save_to_disk=True)
                    self.cortex.connect_entities(file_id, "defines", func_id, save_to_disk=True)
        except Exception:
            pass

    def _analyze_markdown_structure(self, filepath, file_id):
        """Extract headers as knowledge nodes."""
        if not self.cortex: return
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    match = re.match(r'^(#{1,3})\s+(.*)', line)
                    if match:
                        title = match.group(2).strip()
                        safe_title = "".join([c for c in title if c.isalnum() or c == ' ']).strip().replace(' ', '_').lower()
                        if safe_title:
                            concept_id = f"concept_{safe_title}"[:60]
                            self.cortex.add_entity(concept_id, "concept", title, f"Section in {filepath.name}", save_to_disk=True)
                            self.cortex.connect_entities(file_id, "documents", concept_id, save_to_disk=True)
        except Exception:
            pass

    def learn(self, input_file):
        """Legacy single file learning (kept for compatibility)"""
        input_path = Path(input_file)
        if not input_path.exists(): return None
        project_root = self.brain_path.parent.parent
        try:
            self._digest_file(project_root, input_path)
            return f"Ingested {input_path.name} into Graph."
        except Exception as e:
            return f"Error: {e}"
