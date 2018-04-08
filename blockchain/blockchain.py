import datetime
import hashlib
import json
from flask import Flask, jsonify

# Building blockchain architecture
class Blockchain(object):

    # All of the variables referring to each instance of the blockchain object.
    def __init__(self):
        self.chain = []
        # Previous hash is 0 referring to the genesis block.
        self.create_block(proof=1, prev_hash='0')
