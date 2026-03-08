import re
import datetime
from pathlib import Path

class Scholar:
    def __init__(self, brain_path):
        self.brain_path = Path(brain_path)
        self.memories_path = self.brain_path / "memories"

    def learn(self, input_file):
        """Ingest a file, extract patterns, generate record."""
        input_path = Path(input_file)
        if not input_path.exists():
            return None

        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        extracted = self.extract_architecture(content)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        record_filename = f"learning-record-{timestamp}.md"
        record_path = self.memories_path / record_filename

        mode = 'a' if record_path.exists() else 'w'
        with open(record_path, mode, encoding='utf-8') as f:
            if mode == 'w':
                f.write(f"# 🧠 NEXUS CORTEX: Learning Record\n")

            f.write(f"\n> **Date**: {datetime.datetime.now().isoformat()} | **Source**: {input_path.name}\n")
            f.write(f"## 🏛️ Extracted Knowledge\n")
            f.write(f"{extracted}\n")
            f.write(f"---\n")

        return str(record_path)

    def extract_architecture(self, text):
        """Hybrid Extraction: Regex + Semantic Fallback"""

        # 1. Strict Code Patterns
        code_patterns = [
            r'(?i)class\s+(\w+).*?:',
            r'(?i)"(\w+)"\s*:\s*{',
        ]
        extracted_points = []
        for p in code_patterns:
            matches = re.findall(p, text)
            if matches:
                extracted_points.extend([f"- [Code] Found entity: `{m}`" for m in matches[:5]])

        # 2. Semantic Fallback (Prose)
        if not extracted_points:
            # Headers
            semantic_headers = r'(?i)^#+\s*(Overview|Introduction|Architecture|Design|Concepts)'
            header_match = re.search(semantic_headers, text, re.MULTILINE)
            if header_match:
                start = header_match.end()
                fallback_text = text[start:start+1000].strip()
                summary = re.sub(r'[#*`]', '', fallback_text).split('\n\n')[0]
                extracted_points.append(f"- [Core Concept] {summary}...")

            # Definitions "X is a Y"
            definitions = re.findall(r'(?i)\b(\w{3,20})\s+is\s+a\s+(deterministic|distributed|protocol|system|model)', text)
            for term, type_ in definitions[:3]:
                extracted_points.append(f"- [Def] **{term}** defined as *{type_}*")

        if not extracted_points:
            return "> *No structured architecture detected.*"

        return "\n".join(extracted_points)
