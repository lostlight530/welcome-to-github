import sqlite3
import logging
import datetime
from dataclasses import dataclass
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='[Cortex] %(message)s')

@dataclass
class Entity:
    id: str
    type: str
    name: str
    desc: str
    created_at: str = ""
    updated_at: str = ""
    weight: float = 1.0          # 神经权重 (>1.0 = 强化, <1.0 = 衰减)
    last_activated: str = ""     # 上次激活时间 ISO格式

@dataclass
class Relation:
    source: str
    relation: str
    target: str
    annotation: str = ""
    created_at: str = ""
    weight: float = 1.0

class Cortex:
    def __init__(self, db_path: str = "docs/brain/cortex.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.init_db()

    def init_db(self):
        """Initialize the database schema with auto-migration support."""
        cursor = self.conn.cursor()

        # 1. Base Tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entities (
                id TEXT PRIMARY KEY,
                type TEXT,
                name TEXT,
                desc TEXT,
                created_at TEXT,
                updated_at TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS relations (
                source TEXT,
                relation TEXT,
                target TEXT,
                annotation TEXT,
                created_at TEXT,
                weight REAL DEFAULT 1.0,
                PRIMARY KEY (source, relation, target)
            )
        ''')

        # 2. Dynamic Schema Migration (Check for missing columns)
        cursor.execute("PRAGMA table_info(entities)")
        columns = [info[1] for info in cursor.fetchall()]

        if 'weight' not in columns:
            logging.info("Schema Migration: Adding 'weight' to entities...")
            cursor.execute("ALTER TABLE entities ADD COLUMN weight REAL DEFAULT 1.0")

        if 'last_activated' not in columns:
            logging.info("Schema Migration: Adding 'last_activated' to entities...")
            cursor.execute("ALTER TABLE entities ADD COLUMN last_activated TEXT")

        # 3. FTS5 Search Index
        cursor.execute('CREATE VIRTUAL TABLE IF NOT EXISTS entities_fts USING fts5(id, name, desc)')
        self.conn.commit()

    def add_entity(self, entity: Entity):
        cursor = self.conn.cursor()
        now = datetime.datetime.now().isoformat()

        # Upsert logic with Memory Reinforcement
        cursor.execute('''
            INSERT INTO entities (id, type, name, desc, created_at, updated_at, weight, last_activated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                type=excluded.type,
                name=excluded.name,
                desc=excluded.desc,
                updated_at=?,
                weight=weight + 0.2,  -- Re-ingesting reinforces memory
                last_activated=?
        ''', (entity.id, entity.type, entity.name, entity.desc,
              now, now, entity.weight, now,
              now, now))

        # Update search index
        cursor.execute('''
            INSERT OR REPLACE INTO entities_fts (rowid, id, name, desc)
            SELECT rowid, id, name, desc FROM entities WHERE id = ?
        ''', (entity.id,))

        self.conn.commit()

    def add_relation(self, relation: Relation):
        cursor = self.conn.cursor()
        now = datetime.datetime.now().isoformat()
        cursor.execute('''
            INSERT OR REPLACE INTO relations (source, relation, target, annotation, created_at, weight)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (relation.source, relation.relation, relation.target, relation.annotation, now, relation.weight))
        self.conn.commit()

    def search(self, query: str, limit: int = 5) -> List[Dict]:
        """
        Context-Aware Search: Results ranked by FTS rank * (1 / Memory Weight).
        Heavier memories float to the top.
        """
        cursor = self.conn.cursor()
        sql = '''
            SELECT e.* FROM entities_fts f
            JOIN entities e ON f.id = e.id
            WHERE entities_fts MATCH ?
            ORDER BY f.rank * (1.0 / e.weight)
            LIMIT ?
        '''
        try:
            cursor.execute(sql, (query, limit))
            results = [dict(row) for row in cursor.fetchall()]
        except sqlite3.OperationalError:
             # Fallback
             term = f"%{query}%"
             cursor.execute('SELECT * FROM entities WHERE id LIKE ? OR name LIKE ? OR desc LIKE ? ORDER BY weight DESC LIMIT ?', (term, term, term, limit))
             results = [dict(row) for row in cursor.fetchall()]

        # Activate the memories that were retrieved
        for res in results:
            self.activate_memory(res['id'])

        return results

    def get_entity(self, entity_id: str) -> Optional[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM entities WHERE id = ?", (entity_id,))
        row = cursor.fetchone()
        if row:
            self.activate_memory(entity_id) # Accessing memory strengthens it
            return dict(row)
        return None

    def get_relations(self, entity_id: str) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT source, relation, target, weight FROM relations
            WHERE source = ? OR target = ?
        ''', (entity_id, entity_id))
        return [dict(row) for row in cursor.fetchall()]

    # === Neuro-Plasticity Features ===

    def activate_memory(self, entity_id: str, boost: float = 0.5):
        """Reinforce a memory (Synaptic Potentiation)."""
        now = datetime.datetime.now().isoformat()
        cursor = self.conn.cursor()
        # Cap max weight at 5.0 to prevent explosion
        cursor.execute('''
            UPDATE entities
            SET weight = MIN(5.0, weight + ?), last_activated = ?
            WHERE id = ?
        ''', (boost, now, entity_id))
        self.conn.commit()

    def decay_memories(self, decay_rate: float = 0.95):
        """Simulate forgetting (Synaptic Depression)."""
        logging.info("Running Cortical Decay (Sleep Phase)...")
        cursor = self.conn.cursor()
        # Decay everything by 5%, floor at 0.1
        cursor.execute('''
            UPDATE entities
            SET weight = MAX(0.1, weight * ?)
        ''', (decay_rate,))
        self.conn.commit()
        logging.info("Memory weights adjusted.")
