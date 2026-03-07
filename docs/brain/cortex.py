import sqlite3
import json
import time
from pathlib import Path
from typing import List, Dict

class Cortex:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        # Entity Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entities (
                id TEXT PRIMARY KEY,
                type TEXT,
                name TEXT,
                desc TEXT,
                weight REAL DEFAULT 1.0,
                last_activated REAL
            )
        ''')
        # FTS5 Index for full-text search
        cursor.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS entities_fts USING fts5(id, name, desc)
        ''')
        # Relations Table (The Synapses)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS relations (
                source TEXT,
                relation TEXT,
                target TEXT,
                weight REAL DEFAULT 1.0,
                UNIQUE(source, relation, target)
            )
        ''')
        self.conn.commit()

    def search(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Synaptic Associative Search
        结合了 FTS5 全文检索 + 1-Hop 图谱联想。
        """
        cursor = self.conn.cursor()

        # 1. Sanitize & Prefix
        safe_query = "".join(c for c in query if c.isalnum() or c.isspace())
        if not safe_query.strip(): return []
        fts_query = " ".join([f"{token}*" for token in safe_query.split()])

        # 2. Direct Match (FTS5)
        sql_direct = '''
            SELECT e.id, e.name, e.desc, e.weight, 0 as distance
            FROM entities_fts f
            JOIN entities e ON f.id = e.id
            WHERE entities_fts MATCH ?
            ORDER BY f.rank * (1.0 / e.weight)
            LIMIT ?
        '''
        cursor.execute(sql_direct, (fts_query, limit))
        direct_results = [dict(row) for row in cursor.fetchall()]

        if not direct_results: return []

        # 3. Associative Expansion (Graph)
        direct_ids = [r['id'] for r in direct_results]
        placeholders = ','.join(['?'] * len(direct_ids))

        sql_assoc = f'''
            SELECT e.id, e.name, e.desc, e.weight, 1 as distance
            FROM relations r
            JOIN entities e ON (r.target = e.id OR r.source = e.id)
            WHERE (r.source IN ({placeholders}) OR r.target IN ({placeholders}))
            AND e.id NOT IN ({placeholders})
            AND e.weight > 1.1 -- Only strong associations
            ORDER BY e.weight DESC
            LIMIT 3
        '''
        params = direct_ids + direct_ids + direct_ids
        cursor.execute(sql_assoc, params)
        assoc_results = [dict(row) for row in cursor.fetchall()]

        # 4. Merge & Activate
        final_results = direct_results + assoc_results
        for res in final_results:
            boost = 0.2 if res['distance'] == 0 else 0.05
            self.activate_memory(res['id'], boost=boost)

        return final_results

    def add_entity(self, id, type_slug, name, desc):
        cursor = self.conn.cursor()
        now = time.time()
        try:
<<<<<<< HEAD
            cursor.execute('''INSERT INTO entities (id, type, name, desc, weight, last_activated, created_at, updated_at)
                              VALUES (?, ?, ?, ?, 1.0, ?, ?, ?)''',
                          (id, type_slug, name, desc, now, now, now))
=======
            cursor.execute('INSERT INTO entities VALUES (?, ?, ?, ?, 1.0, ?)',
                          (id, type_slug, name, desc, now))
>>>>>>> main
            cursor.execute('INSERT INTO entities_fts VALUES (?, ?, ?)', (id, name, desc))
            self.conn.commit()
        except sqlite3.IntegrityError:
            self.activate_memory(id)

    def connect_entities(self, source, relation, target, desc=""):
        cursor = self.conn.cursor()
<<<<<<< HEAD
        now = time.time()
        try:
            cursor.execute('''INSERT INTO relations (source, relation, target, weight, annotation, created_at)
                              VALUES (?, ?, ?, 1.0, ?, ?)''',
                          (source, relation, target, desc, now))
=======
        try:
            cursor.execute('INSERT INTO relations VALUES (?, ?, ?, 1.0)',
                          (source, relation, target))
>>>>>>> main
            self.conn.commit()
            # Strengthen both nodes
            self.activate_memory(source, 0.1)
            self.activate_memory(target, 0.1)
        except sqlite3.IntegrityError:
            pass

    def activate_memory(self, id, boost=0.1):
        cursor = self.conn.cursor()
        now = time.time()
        cursor.execute('UPDATE entities SET weight = weight + ?, last_activated = ? WHERE id = ?',
                      (boost, now, id))
        self.conn.commit()

    def decay_memories(self, decay_rate=0.95):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE entities SET weight = weight * ? WHERE weight > 0.1', (decay_rate,))
        self.conn.commit()

    def get_orphans(self, limit=5):
        cursor = self.conn.cursor()
        # Find entities with NO relations (in or out)
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

    def get_entity(self, entity_id: str) -> Dict:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM entities WHERE id = ?", (entity_id,))
        row = cursor.fetchone()
        if row:
            self.activate_memory(entity_id)
            return dict(row)
        return None

    def get_stats(self):
        cursor = self.conn.cursor()
        e_count = cursor.execute('SELECT count(*) FROM entities').fetchone()[0]
        r_count = cursor.execute('SELECT count(*) FROM relations').fetchone()[0]
        avg_weight = cursor.execute('SELECT avg(weight) FROM entities').fetchone()[0] or 0
        return {'entities': e_count, 'relations': r_count, 'density': avg_weight}
