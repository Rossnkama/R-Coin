from flask import Flask, jsonify
from blockchain import blockchainArch

# Creating a Web App
app = Flask(__name__)

# Creating our blockchain
blockchain = blockchainArch.Blockchain()


# Mining a new block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    """ Miner's will use this method to mine for blocks in the blockchain.

        :return: Congrats message with block metadata, HTTP status
        :rtype: object, int
    """
    previous_block = blockchain.get_prev_block()
    previous_nonce = previous_block['nonce']

    # Now the next block's nonce is calculated from the precious nonce
    next_block_nonce = blockchain.proof_of_work(previous_nonce)
    previous_hash = blockchain.hash(previous_block)

    # Creating mined block
    next_block = blockchain.create_block(next_block_nonce, previous_hash)

    response = {
        'Message': 'Congratulations, you just mined a block!',
        'index': next_block['index'],
        'timestamp': next_block['timestamp'],
        'proof': next_block['nonce'],
        'previous_hash': next_block['prev_hash']
    }

    # JSON of response and a HTTP status of (200 OK)
    return jsonify(response), 200


# Getting the entire blockchain's ledger
@app.route('/get_chain', methods=['GET'])
def get_chain():
    """ Miner's will use this to their own copy of the entire blockchain

            :return: Some blockchain metadata, HTTP status
            :rtype: object, int
    """
    response = {
        'Blockchain': blockchain.chain,
        'Blockchain length': len(blockchain.chain)
    }
    return jsonify(response), 200
