import hashlib
import json
import time
from typing import List, Dict, Any

class Block:
    def __init__(self, index: int, timestamp: float, transactions: List[Dict], previous_hash: str, nonce: int = 0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty: int):
        target = '0' * difficulty
        while self.hash[:difficulty]!= target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.pending_transactions: List[Dict] = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, time.time(), [{"genesis": True}], "0")
        genesis.mine_block(self.difficulty)
        self.chain.append(genesis)

    def get_last_block(self) -> Block:
        return self.chain[-1]

    def add_transaction(self, sender: str, recipient: str, amount: float):
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
            "timestamp": time.time()
        })

    def mine_pending_transactions(self, miner_address: str):
        if not self.pending_transactions:
            return False
        
        block = Block(
            len(self.chain),
            time.time(),
            self.pending_transactions,
            self.get_last_block().hash
        )
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = []
        return True

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash!= current.calculate_hash():
                return False
            if current.previous_hash!= previous.hash:
                return False
        return True