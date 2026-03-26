import sqlite3
import json
import time
import datetime
from pathlib import Path
from typing import List, Dict

class Cortex:
    def __init__(self, db_path):
        self.brain_path = Path(db_path).parent
        self.db_path = db_path
        self.knowledge_path = self.brain_path / "knowledge"

        # Ensure knowledge structure exists
        (self.knowledge_path / "entities").mkdir(parents=True, exist_ok=True)
        (self.knowledge_path / "relations").mkdir(parents=True, exist_ok=True)

        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

        # [v2.3 Core Axioms] The Memory Whitelist
        # These concepts are "Axioms" - they define the system's identity.
        # They are immune to biological decay.
        self.CORE_WHITELIST = {
            "agent", "mcp", "edge-ai", "nexus", "sovereignty",
            "mindspore", "litert", "mediapipe", "zerodependency",
            "jax-metal", "eurobert", "android", "vllm", "dify"
        }
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        # Phase IV.1: Temporal Knowledge Graph Schema
        # Dropped PRIMARY KEY on id, introduced composite (id, valid_at) and invalid_at for 4D tracking.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entities (
                id TEXT,
                type TEXT,
                name TEXT,
                desc TEXT,
                weight REAL DEFAULT 1.0,
                last_activated REAL,
                valid_at TEXT,
                invalid_at TEXT,
                PRIMARY KEY (id, valid_at)
            )
        ''')
        # Deterministic Temporal Index for Entities
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_entities_temporal
            ON entities (id, invalid_at)
        ''')

        cursor.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS entities_fts USING fts5(id, name, desc)
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS relations (
                source TEXT,
                relation TEXT,
                target TEXT,
                weight REAL DEFAULT 1.0,
                valid_at TEXT,
                invalid_at TEXT,
                UNIQUE(source, relation, target, valid_at)
            )
        ''')
        # Deterministic Temporal Index for Relations
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_relations_temporal
            ON relations (source, target, invalid_at)
        ''')
        self.conn.commit()

    def _log_to_jsonl(self, category, filename, data):
        """Append knowledge to the immutable text ledger."""
        # Sanitize filename to prevent directory traversal or invalid chars
        safe_filename = "".join([c for c in filename if c.isalnum() or c in ('-','_')])
        if not safe_filename: safe_filename = "misc"

        filepath = self.knowledge_path / category / f"{safe_filename}.jsonl"
        try:
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False) + "\n")
        except Exception as e:
            print(f"⚠️ Failed to write text memory: {e}")

    def search(self, query: str, limit: int = 10) -> List[Dict]:
        """Synaptic Search: Combines Full-Text + 1-Hop Graph Association"""
        cursor = self.conn.cursor()
        safe_query = "".join(c for c in query if c.isalnum() or c.isspace())
        if not safe_query.strip(): return []
        fts_query = " ".join([f"{token}*" for token in safe_query.split()])

        # 1. Direct Match (FTS5) - Only return actively valid memories
        sql_direct = '''
            SELECT e.id, e.name, e.desc, e.weight, 0 as distance
            FROM entities_fts f
            JOIN entities e ON f.id = e.id
            WHERE entities_fts MATCH ? AND e.invalid_at IS NULL
            ORDER BY f.rank * (1.0 / e.weight)
            LIMIT ?
        '''
        cursor.execute(sql_direct, (fts_query, limit))
        direct_results = [dict(row) for row in cursor.fetchall()]

        if not direct_results: return []

        # 2. Associative Expansion (Graph) - Only explore valid topological bounds
        direct_ids = [r['id'] for r in direct_results]
        placeholders = ','.join(['?'] * len(direct_ids))

        sql_assoc = f'''
            SELECT e.id, e.name, e.desc, e.weight, 1 as distance
            FROM relations r
            JOIN entities e ON (r.target = e.id OR r.source = e.id)
            WHERE (r.source IN ({placeholders}) OR r.target IN ({placeholders}))
            AND e.id NOT IN ({placeholders})
            AND e.weight > 1.1
            AND e.invalid_at IS NULL
            AND r.invalid_at IS NULL
            ORDER BY e.weight DESC
            LIMIT 3
        '''
        params = direct_ids + direct_ids + direct_ids
        cursor.execute(sql_assoc, params)
        assoc_results = [dict(row) for row in cursor.fetchall()]

        return direct_results + assoc_results

    def add_entity(self, id, type_slug, name, desc, save_to_disk=True):
        cursor = self.conn.cursor()
        now = time.time()
        now_iso = datetime.datetime.utcnow().isoformat()
        w = 2.0 if id in self.CORE_WHITELIST else 1.0

        # Phase IV.1: Temporal Override
        # If entity exists and is identical, do nothing. If different, mark invalid and insert new.
        cursor.execute('SELECT type, name, desc FROM entities WHERE id = ? AND invalid_at IS NULL', (id,))
        existing = cursor.fetchone()
        if existing:
            if existing['type'] == type_slug and existing['name'] == name and existing['desc'] == desc:
                # Same record, just update last_activated
                cursor.execute('UPDATE entities SET last_activated = ? WHERE id = ? AND invalid_at IS NULL', (now, id))
                self.conn.commit()
                return True
            else:
                cursor.execute('UPDATE entities SET invalid_at = ? WHERE id = ? AND invalid_at IS NULL', (now_iso, id))

        try:
            cursor.execute('INSERT INTO entities VALUES (?, ?, ?, ?, ?, ?, ?, NULL)',
                          (id, type_slug, name, desc, w, now, now_iso))

            # FTS5 doesn't need temporal tracking natively since it joins back, but we clear and re-insert
            cursor.execute('DELETE FROM entities_fts WHERE id = ?', (id,))
            cursor.execute('INSERT INTO entities_fts VALUES (?, ?, ?)', (id, name, desc))

            self.conn.commit()

            # [Dual-Write Control] Temporal JSONL
            if save_to_disk:
                self._log_to_jsonl("entities", type_slug, {
                    "id": id, "type": type_slug, "name": name, "desc": desc, "valid_at": now_iso
                })

        except sqlite3.IntegrityError:
            self.activate_memory(id)

    def connect_entities(self, source, relation, target, desc="", save_to_disk=True):
        cursor = self.conn.cursor()
        now_iso = datetime.datetime.utcnow().isoformat()

        # Check if identical relation exists actively
        cursor.execute('''
            SELECT 1 FROM relations
            WHERE source = ? AND relation = ? AND target = ? AND invalid_at IS NULL
        ''', (source, relation, target))
        if cursor.fetchone():
            return True # Already exists and active, do nothing to prevent unnecessary invalidation

        # Temporal Invalidation: Overwrite edge if it exists logically but temporal forces soft delete
        cursor.execute('''
            UPDATE relations SET invalid_at = ?
            WHERE source = ? AND relation = ? AND target = ? AND invalid_at IS NULL
        ''', (now_iso, source, relation, target))

        try:
            cursor.execute('INSERT INTO relations VALUES (?, ?, ?, 1.0, ?, NULL)',
                          (source, relation, target, now_iso))
            self.conn.commit()
            self.activate_memory(source, 0.1)
            self.activate_memory(target, 0.1)

            # [Dual-Write Control] Temporal JSONL
            if save_to_disk:
                month_str = datetime.datetime.now().strftime("%Y-%m")
                self._log_to_jsonl("relations", month_str, {
                    "src": source, "relation": relation, "dst": target, "desc": desc, "valid_at": now_iso
                })

        except sqlite3.IntegrityError:
            pass

    def activate_memory(self, id, boost=0.1):
        cursor = self.conn.cursor()
        now = time.time()
        cursor.execute('UPDATE entities SET weight = weight + ?, last_activated = ? WHERE id = ? AND invalid_at IS NULL',
                      (boost, now, id))
        self.conn.commit()

    def decay_memories(self, decay_rate=0.95):
        """Biological Decay with Sovereignty Protection"""
        cursor = self.conn.cursor()

        # 1. Universal Decay
        cursor.execute('UPDATE entities SET weight = weight * ? WHERE weight > 0.1', (decay_rate,))

        # 2. Whitelist Restoration (Sovereignty Check)
        if self.CORE_WHITELIST:
            placeholders = ','.join(['?'] * len(self.CORE_WHITELIST))
            sql_restore = f'''
                UPDATE entities SET weight = 1.2
                WHERE id IN ({placeholders}) AND weight < 1.2
            '''
            cursor.execute(sql_restore, list(self.CORE_WHITELIST))

        self.conn.commit()

    def get_orphans(self, limit=5):
        cursor = self.conn.cursor()
        sql = '''
            SELECT e.id, e.name, e.weight FROM entities e
            LEFT JOIN relations r1 ON e.id = r1.source
            LEFT JOIN relations r2 ON e.id = r2.target
            WHERE r1.source IS NULL AND r2.target IS NULL
            AND e.weight > 0.5
            ORDER BY e.weight DESC
            LIMIT ?
        '''
        cursor.execute(sql, (limit,))
        return [dict(row) for row in cursor.fetchall()]

    def get_stats(self):
        cursor = self.conn.cursor()
        try:
            e_count = cursor.execute('SELECT count(*) FROM entities').fetchone()[0]
            r_count = cursor.execute('SELECT count(*) FROM relations').fetchone()[0]
            avg_weight = cursor.execute('SELECT avg(weight) FROM entities').fetchone()[0] or 0
        except:
            return {'entities': 0, 'relations': 0, 'density': 0}
        return {'entities': e_count, 'relations': r_count, 'density': avg_weight}