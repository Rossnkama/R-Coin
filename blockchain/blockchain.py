import datetime
import hashlib
import json
from flask import Flask, jsonify

# Building blockchain architecture


class Blockchain(object):
    def __init__(self):
        """ Initialisation of the blockchain and genesis block.
            These are all of the variables referring to each instance of the blockchain object:

            :type self.chain: list
        """
        self.chain = []
        # Previous hash is 0 referring to the creation of genesis block at initialisation.
        self.create_block(proof=1, prev_hash='0')

    def create_block(self, proof, prev_hash):
        """ Simply creates a block with the work retrieved after mining the block
            and then appends it to the blockchain.

            :param proof: The hash of the current block
            :type proof: int

            :param prev_hash: The hash of block[i-1]
            :type prev_hash: str

            :return:
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'prev_hash': prev_hash
        }
        self.chain.append(block)
        return block  # For postman

    def get_prev_block(self):
        return self.chain[-1]

    @staticmethod
    def proof_of_work(prev_nonce):
        """ I will determine the common algorithm miners will use for PoW so only hashing power
            in terms of hardware will determine how fast a golden hash is mined.

            :param prev_nonce: Nonce of previous block
            :type prev_nonce: int

            :return: new_nonce, The nonce that was used to attain the golden hash.
        """
        new_nonce = 1
        check_proof = False

        while not check_proof:
            # A non-symmetrical/non-commutative operation between the new and previous nonce proof
            # This prevents every 2 blocks from having the same
            hash_operation = hashlib.sha256(
                str(new_nonce**2 - prev_nonce**2).encode()  # Squaring the nonce to make mining a little harder
            ).hexdigest()

            if hash_operation[0:4] == '0000':
                check_proof = True
            new_nonce += 1

        return new_nonce

    @staticmethod
    def hash(block):
        """ This hashes a block's jsonfied dictionary.

            :param block: A block in the blockchain
            :type block: dict

            :return: <str>: SHA256(block)
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

