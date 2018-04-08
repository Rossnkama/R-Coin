from flask import Flask, jsonify
from blockchain import blockchainArch

# Creating a Web App
app = Flask(__name__)


# Creating our blockchain
blockchain = blockchainArch.Blockchain()
