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
            'inputs', '.raw_cache', 'knowledge', 'archaeology', 'venv', '.idea', '.vscode', 'site-packages'
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

        # 2. Deep Content Analysis (Polyglot Regex + AST)
        if filepath.suffix == '.py':
            self._analyze_python_ast(filepath, file_id)
        elif filepath.suffix in ['.js', '.jsx', '.ts', '.tsx']:
            self._analyze_javascript_regex_ast(filepath, file_id)
        elif filepath.suffix == '.md':
            self._analyze_markdown_structure(filepath, file_id)
        elif filepath.suffix in ['.json', '.yaml', '.yml']:
            self._analyze_config_structure(filepath, file_id)

    def _analyze_config_structure(self, filepath, file_id):
        """Phase IV: Universal Digestion. Extracts deterministic properties from JSON/YAML configurations."""
        if not self.cortex: return
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            data = None
            if filepath.suffix == '.json':
                data = json.loads(content)
            elif filepath.suffix in ['.yaml', '.yml']:
                # Zero-dependency Stack-based YAML parser for multi-level dicts/lists
                data = {}
                stack = [(-1, data, None)] # (indent, current_obj, current_key)

                for line in content.splitlines():
                    if not line.strip() or line.strip().startswith('#'):
                        continue

                    indent = len(line) - len(line.lstrip())
                    clean_line = line.strip()

                    # Pop stack until we find parent
                    while stack and stack[-1][0] >= indent:
                        stack.pop()

                    parent_obj = stack[-1][1] if stack else data

                    # Handle list item
                    if clean_line.startswith('- '):
                        val = clean_line[2:].strip()
                        if isinstance(parent_obj, list):
                            parent_obj.append(val)
                        else:
                            # Edge case: key followed by list
                            key = stack[-1][2]
                            if key and stack[-2][1].get(key) is None:
                                stack[-2][1][key] = [val]
                                stack.pop()
                                stack.append((indent, stack[-1][1][key], None))
                    # Handle key-value or key-dict
                    elif ':' in clean_line:
                        key, val = [part.strip() for part in clean_line.split(':', 1)]
                        # Clean quotes
                        if val and val[0] in ('"', "'") and val[-1] == val[0]:
                            val = val[1:-1]

                        if not val:
                            new_dict = {}
                            if isinstance(parent_obj, dict):
                                parent_obj[key] = new_dict
                            stack.append((indent, new_dict, key))
                        else:
                            if isinstance(parent_obj, dict):
                                parent_obj[key] = val

            def _extract_props(obj, parent_key=""):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        new_key = f"{parent_key}.{k}" if parent_key else k
                        _extract_props(v, new_key)
                elif isinstance(obj, list):
                    for idx, v in enumerate(obj):
                        new_key = f"{parent_key}[{idx}]"
                        _extract_props(v, new_key)
                elif isinstance(obj, (str, int, float, bool)):
                    prop_id = f"{file_id}_prop_{parent_key.replace('.', '_').replace('[', '_').replace(']', '')}"
                    desc = str(obj)[:100]
                    self.cortex.add_entity(prop_id, "config_property", parent_key, desc, save_to_disk=True)
                    self.cortex.connect_entities(file_id, "defines", prop_id, save_to_disk=True)

            if isinstance(data, dict):
                _extract_props(data)
        except Exception as e:
            print(f"      [Config Error] {filepath.name}: {e}")

    def _analyze_javascript_regex_ast(self, filepath, file_id):
        """Polyglot Deterministic Extraction: Simulating Tree-sitter using zero-dependency Regex for JS/TS."""
        if not self.cortex: return
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract Classes (e.g., class MyComponent extends React.Component)
            class_pattern = re.compile(r'class\s+([A-Za-z0-9_]+)(?:\s+extends\s+([A-Za-z0-9_.]+))?\s*\{')
            for match in class_pattern.finditer(content):
                class_name = match.group(1)
                base_class = match.group(2)
                class_id = f"class_{class_name}"
                self.cortex.add_entity(class_id, "code_class", class_name, f"JS/TS Class in {filepath.name}", save_to_disk=True)
                self.cortex.connect_entities(file_id, "defines", class_id, save_to_disk=True)
                if base_class:
                    self.cortex.connect_entities(class_id, "inherits_from", f"class_{base_class.replace('.', '_')}", save_to_disk=True)

            # Extract Functions (function myFunc() or const myFunc = () =>)
            func_pattern = re.compile(r'(?:function\s+([A-Za-z0-9_]+)\s*\()|(?:(?:const|let|var)\s+([A-Za-z0-9_]+)\s*=\s*(?:async\s+)?(?:\([^)]*\)|[A-Za-z0-9_]+)\s*=>)')
            for match in func_pattern.finditer(content):
                func_name = match.group(1) or match.group(2)
                if func_name:
                    func_id = f"func_{func_name}"
                    self.cortex.add_entity(func_id, "code_function", func_name, f"JS/TS Function in {filepath.name}", save_to_disk=True)
                    self.cortex.connect_entities(file_id, "defines", func_id, save_to_disk=True)

        except Exception as e:
            print(f"      [Polyglot Error] {filepath.name}: {e}")

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
