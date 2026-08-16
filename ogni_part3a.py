import requests
from urllib.parse import urlparse

class P2PNetwork:
    def __init__(self):
        self.nodes = set()

    def register_node(self, address: str):
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    def resolve_conflicts(self, blockchain):
        neighbours = self.nodes
        new_chain = None
        max_length = len(blockchain.chain)

        for node in neighbours:
            try:
                response = requests.get(f'http://{node}/chain')
                if response.status_code == 200:
                    length = response.json()['length']
                    chain = response.json()['chain']
                    if length > max_length and self.valid_chain(chain):
                        max_length = length
                        new_chain = chain
            except:
                continue

        if new_chain:
            blockchain.chain = [self.dict_to_block(b) for b in new_chain]
            return True
        return False

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            if block['previous_hash']!= last_block['hash']:
                return False
            last_block = block
            current_index += 1
        return True

    def dict_to_block(self, block_dict):
        from igni_part1 import Block # CORRIGIDO AQUI
        block = Block(
            block_dict['index'],
            block_dict['timestamp'],
            block_dict['transactions'],
            block_dict['previous_hash'],
            block_dict['nonce']
        )
        block.hash = block_dict['hash']
        return block