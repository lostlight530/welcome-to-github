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

    def search(self, query: str, limit: int = 10) -> List[Dict]:
        """
        [v2.1 Upgrade] Synaptic Associative Search (突触联想搜索)
        结合了 FTS5 全文检索 + 1-Hop 图谱联想。
        """
        cursor = self.conn.cursor()

        # === 1. Pre-process Query (Sanitization & Prefix) ===
        # 移除特殊字符，防止 FTS5 语法错误
        safe_query = "".join(c for c in query if c.isalnum() or c.isspace())
        if not safe_query.strip(): return []

        # 构造前缀查询: "vllm up" -> "vllm* up*" (支持部分匹配)
        fts_query = " ".join([f"{token}*" for token in safe_query.split()])

        # === 2. Direct Search (FTS5) ===
        # 找到字面匹配的节点
        sql_direct = '''
            SELECT e.id, e.name, e.desc, e.weight, 0 as distance
            FROM entities_fts f
            JOIN entities e ON f.id = e.id
            WHERE entities_fts MATCH ?
            ORDER BY f.rank * (1.0 / e.weight) -- 权重越高，Rank数值越小(越靠前)
            LIMIT ?
        '''
        try:
            cursor.execute(sql_direct, (fts_query, limit))
            direct_results = [dict(row) for row in cursor.fetchall()]
        except sqlite3.OperationalError:
            # Fallback for unexpected FTS syntax errors
            term = f"%{safe_query}%"
            cursor.execute('''
                SELECT id, name, desc, weight, 0 as distance
                FROM entities
                WHERE id LIKE ? OR name LIKE ? OR desc LIKE ?
                ORDER BY weight DESC LIMIT ?
            ''', (term, term, term, limit))
            direct_results = [dict(row) for row in cursor.fetchall()]

        if not direct_results:
            return []

        # === 3. Associative Search (Graph Expansion) ===
        # 找到与直搜结果强关联的邻居 (Brainstorming)
        direct_ids = [r['id'] for r in direct_results]
        placeholders = ','.join(['?'] * len(direct_ids))

        sql_assoc = f'''
            SELECT e.id, e.name, e.desc, e.weight, 1 as distance
            FROM relations r
            JOIN entities e ON (r.target = e.id OR r.source = e.id)
            WHERE (r.source IN ({placeholders}) OR r.target IN ({placeholders}))
            AND e.id NOT IN ({placeholders}) -- 排除自己
            AND e.weight > 1.2 -- 只联想"重要"的概念 (Weight > 1.2)
            ORDER BY e.weight DESC
            LIMIT 3 -- 限制联想数量，避免噪声
        '''

        # 参数需要传两次 direct_ids (一次给 source IN, 一次给 target IN) + 排除用
        params = direct_ids + direct_ids + direct_ids
        cursor.execute(sql_assoc, params)
        assoc_results = [dict(row) for row in cursor.fetchall()]

        # === 4. Merge & Activate ===
        final_results = direct_results + assoc_results

        # 激活被检索到的记忆 (Reinforce)
        for res in final_results:
            # 联想出的结果加权少一点 (0.1)，直搜的加权多一点 (0.5)
            boost = 0.5 if res['distance'] == 0 else 0.1
            self.activate_memory(res['id'], boost=boost)

            # 标记来源给 UI/CLI
            res['source'] = '🔍 Match' if res['distance'] == 0 else '🔗 Link'

        return final_results

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
