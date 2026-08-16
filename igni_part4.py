import sqlite3
import os

class Database:
    def __init__(self, db_name='data/blockchain.db'):
        os.makedirs('data', exist_ok=True)
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS blocks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                block_index INTEGER UNIQUE,
                timestamp REAL,
                hash TEXT UNIQUE,
                previous_hash TEXT,
                nonce INTEGER,
                data TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT,
                recipient TEXT,
                amount REAL,
                timestamp REAL,
                block_index INTEGER
            )
        ''')
        self.conn.commit()

    def save_block(self, block):
        self.cursor.execute('''
            INSERT OR REPLACE INTO blocks 
            (block_index, timestamp, hash, previous_hash, nonce, data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (block.index, block.timestamp, block.hash, block.previous_hash, block.nonce, str(block.transactions)))
        
        for tx in block.transactions:
            self.cursor.execute('''
                INSERT INTO transactions (sender, recipient, amount, timestamp, block_index)
                VALUES (?, ?, ?)
            ''', (tx.get('sender'), tx.get('recipient'), tx.get('amount'), tx.get('timestamp'), block.index))
        self.conn.commit()

    def load_chain(self):
        self.cursor.execute('SELECT * FROM blocks ORDER BY block_index')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()