from flask import send_from_directory
from flask import Flask, request, jsonify
from igni_part1 import Blockchain
import uuid

app = Flask(__name__)
node_identifier = str(uuid.uuid4()).replace('-', '')
blockchain = Blockchain(difficulty=4)

@app.route('/mine', methods=['GET'])
def mine():
    blockchain.mine_pending_transactions(node_identifier)
    last_block = blockchain.get_last_block()
    response = {
        'message': "Novo bloco minerado",
        'index': last_block.index,
        'hash': last_block.hash,
        'transactions': last_block.transactions,
        'nonce': last_block.nonce
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    
    blockchain.add_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f"Transação será adicionada ao Bloco {blockchain.get_last_block().index + 1}"}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'transactions': block.transactions,
            'hash': block.hash,
            'previous_hash': block.previous_hash,
            'nonce': block.nonce
        })
    response = {
        'chain': chain_data,
        'length': len(chain_data),
    }
    return jsonify(response), 200

@app.route('/valid', methods=['GET'])
def valid():
    is_valid = blockchain.is_chain_valid()
    response = {'valid': is_valid}
    return jsonify(response), 200

@app.route('/')
def home():
    return send_from_directory('', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)