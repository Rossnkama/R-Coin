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
        self.create_block(nonce=1, prev_hash='0')

    def create_block(self, nonce, prev_hash):
        """ Simply creates a block with the work retrieved after mining the block
            and then appends it to the blockchain.

            :param nonce: The hash of the current block
            :type nonce: int

            :param prev_hash: The hash of block[i-1]
            :type prev_hash: str

            :return: A new block
            :rtype: dict
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'nonce': nonce,
            'prev_hash': prev_hash
        }
        self.chain.append(block)
        return block  # For postman

    def get_prev_block(self):
        return self.chain[-1]

    @staticmethod
    def proof_of_work(prev_nonce):
        """ The algorithms miner's will use to find the nonce which gives us the golden hash.

            I will determine the common algorithm miners will use for PoW so only hashing power
            in terms of hardware will determine how fast a golden hash is mined.

            :param prev_nonce: Nonce of previous block
            :type prev_nonce: int

            :return: new_nonce, The nonce that was used to attain the golden hash.
            :rtype: int
        """
        new_nonce = 1
        check_proof = False

        while not check_proof:
            # A non-symmetrical/non-commutative operation between the new and previous nonce proof
            # This prevents every 2 blocks from having the same
            hash_operation = hashlib.sha256(
                str(new_nonce ** 2 - prev_nonce ** 2).encode()  # Squaring the nonce to make mining a little harder
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

            :return: SHA256(block)
            :rtype: str
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, blockchain):
        """ Checks if a system's blockchain is valid (Properly cryptographically linked)

            :param blockchain: The blockchain of whatever system to be checked

            :return: If the blockchain is valid
            :rtype: bool
        """
        block_index = 1
        previous_block = blockchain[0]
        while block_index < len(blockchain):
            current_block = blockchain[block_index]

            # Checking for cryptographic link
            if current_block['prev_hash'] != self.hash(previous_block):
                return False

            # Checking that proof is valid --> is 0000....f or lower
            previous_nonce = previous_block['nonce']
            current_nonce = current_block['nonce']

            # Performs a hash operation on current and prev nonce
            hash_operation = hashlib.sha256(
                str(current_nonce ** 2 - previous_nonce ** 2).encode()
            ).hexdigest()

            if hash_operation[0:4] != '0000':
                return False
            previous_block = current_block
            block_index += 1
        return True
