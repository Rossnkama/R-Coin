import datetime
import hashlib
import json
from flask import Flask, jsonify

# Building blockchain architecture


class Blockchain(object):
    def __init__(self):
        """ Initialisation of the blockchain and genesis block.
            These are all of the variables referring to each instance of the blockchain object:

            :type self.chain: <list>
        """
        self.chain = []
        # Previous hash is 0 referring to the creation of genesis block at initialisation.
        self.create_block(proof=1, prev_hash='0')

    def create_block(self, proof, prev_hash):
        """ Simply creates a block with the work retrieved after mining the block
            and then appends it to the blockchain.

            :param proof: The hash of the current block
            :type proof: int

            :param prev_hash: The has of block[i-1]
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
