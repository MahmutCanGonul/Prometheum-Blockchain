 
# Module 2 - Create a Cryptocurrency

# To be installed:
# Flask==0.12.2: pip install Flask==0.12.2
# Postman HTTP Client: https://www.getpostman.com/
# requests==2.18.4: pip install requests==2.18.4

# Importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse
# Part 1 - Building a Blockchain

from_account = ""
to_account = ""
value = 0
hold_transactions=[]

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof = 1, previous_hash = '0')
        self.nodes = set()
    
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions}
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender': sender,
                                  'receiver': receiver,
                                  'amount': amount})
        
        hold_transactions.append({'sender': sender,
                                  'receiver': receiver,
                                  'amount': amount})    
        previous_block = self.get_previous_block()
        return previous_block['index'] + 1
    
    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
    
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False
  
    
        
        

 
        
             
# Part 2 - Mining our Blockchain

# Creating a Web App
app = Flask(__name__)
 
# Creating an address for the node on Port 5000
 
"""
node_address = str(uuid4()).replace('-', '')
print("This is your address: " + node_address)
"""
node_address = "f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0" #This is our address for send the user Pro coin
# Creating a Blockchain
blockchain = Blockchain()
accounts = []

@app.route('/control_account',methods=['POST'])  #If user enter a public address and private key this account is valid or not
def control_account():
    json = request.get_json()
    account_keys = ['your_address','your_private_key']
    if not all(key in json for key in account_keys):
        return 'Account is not valid!', 400
    is_valid = False
    for i in range(len(accounts)):
        data = accounts[i].split(',')
        if json['your_address'] == data[0] and json['your_private_key'] == data[1]:
            is_valid = True
            break
    
    if is_valid:
        response = {'message':True}
        return jsonify(response),201
    else:
        response = {'message':False}
        return jsonify(response),201


@app.route('/control_address',methods=['POST'])  #If user enter a public address and  this address is  valid or not
def control_address():
    json = request.get_json()
    account_keys = ['address']
    if not all(key in json for key in account_keys):
        return 'Address is not valid!', 400
    
    is_valid =False
    for i in range(len(accounts)):
        data = accounts[i].split(',')
        if json['address'] == data[0]:
            is_valid = True
            break
    if is_valid:
        response = {'message':True}
        return jsonify(response),201
    else:
        response = {'message':False}
        return jsonify(response),201


@app.route('/get_messages',methods=['POST'])   #Get the specific message from the address
def get_special_messages():
    json = request.get_json()
    message_keys = ['address','other_address']
    if not all(key in json for key in message_keys):
        return 'Address is not valid!', 400
    messages = []
    messages2 = []
    
    for i in range(len(hold_transactions)):
        trans = hold_transactions[i]
        if json['address'] == trans['receiver'] and json['other_address'] == trans['sender']:
                data = trans['amount'].split(',')
                if len(data) > 0:
                    if data[0] != "f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0":
                        messages.append(trans['amount'])
                else:
                    messages.append(trans['amount'])
        if json['address'] == trans['sender'] and json['other_address'] == trans['receiver']:
                data = trans['amount'].split(',')
                if len(data) > 0:
                    if data[0] != "f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0":
                        messages2.append(trans['amount'])
                else:
                    messages2.append(trans['amount'])
                    
        
    """
    for i in range(len(blockchain.chain)):
        block = blockchain.chain[i]
        for j in range(len(block['transactions'])):
            trans = block['transactions'][j]
            if json['address'] == trans['receiver'] and json['other_address'] == trans['sender']:
                messages.append(trans['amount'])
            if json['address'] == trans['sender'] and json['other_address'] == trans['receiver']:
                messages2.append(trans['amount'])
    """        
    
    response = {'receiver_message':messages,'sender_message':messages2}
    return jsonify(response),201
    
            
@app.route('/get_all_address',methods = ['GET'])
def get_all_address():
    address = []
    for i in range(len(accounts)):
        data = accounts[i].split(',')
        address.append(data[0])
    response = {'accounts':address}
    return jsonify(response), 200            
    
    
@app.route('/get_all_message_number',methods = ['GET'])
def get_all_message_number():
    sum_of_message=0
    for i in range(len(blockchain.chain)):
        trans = blockchain.chain[i]
        sum_of_message += len(trans['transactions'])
    
    response = {'message_number':sum_of_message}
    return jsonify(response),200
    

        
""" 
@app.route('/get_balance',methods=['POST'])   #Get the balance from the address
def get_balance():
    json = request.get_json()
    account_keys = ['address']
    if not all(key in json for key in account_keys):
        return 'Address is not valid!', 400
    
    balance=0
    for i in range(len(blockchain.chain)):
        chain = blockchain.chain[i]
        for j in range(len(chain['transactions'])):
             trans = chain['transactions'][j]
             if trans['sender'] == json['address']:
                  balance-=1
             if trans['receiver'] == json['address']:
                  balance+=1
    response = {'balance':balance}
    return jsonify(response),201
             
"""
@app.route('/get_balance',methods=['POST'])   #Get the balance from the address
def get_balance():
    json = request.get_json()
    account_keys = ['address']
    if not all(key in json for key in account_keys):
        return 'Address is not valid!', 400
    
    balance=0
    for i in range(len(hold_transactions)):
        trans = hold_transactions[i]
        if trans['receiver'] == json['address'] and trans['sender'] == "f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0":
                 if float(trans['amount']):
                     balance+= float(trans['amount'])
        elif trans['receiver'] == json['address']:
                  if 'f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0' in trans['amount']:
                      balances = trans['amount'].split(',')
                      balance+=float(balances[len(balances)-1])
        elif trans['sender'] == json['address']:
                  if 'f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0' in trans['amount']:
                      balances = trans['amount'].split(',')
                      balance-=float(balances[len(balances)-1])

    response = {'balance':balance}
    return jsonify(response),201


@app.route('/get_address_coming_message',methods=['POST'])
def get_address_coming_message():
    json = request.get_json()
    address = []
    account_keys = ['address']
    if not all(key in json for key in account_keys):
        return 'Address is not valid!', 400
    for i in range(len(hold_transactions)):
        trans = hold_transactions[i]
        if trans['receiver'] == json['address'] and trans['sender'] != 'f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0':
            if not 'f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0' in trans['amount']:
                address.append(trans['sender'])
    response = {'addresslist':address}
    return jsonify(response),201
                

@app.route('/get_block_hash',methods=['GET'])
def get_block_hash():
    hashes = []
    for i in range(len(blockchain.chain)):
        block = blockchain.chain[i]
        hashes.append(block['previous_hash'])
    response ={"hash":hashes}
    return jsonify(response),200
   

      
@app.route('/generate_account',methods = ['POST'])
def generate_account():
    json = request.get_json()
    account_keys = ['address','private_key']
    if not all(key in json for key in account_keys):
        return 'Generate Account Issue', 400
    data = json['address']+","+json['private_key']
    accounts.append(data)
    last_account = accounts[len(accounts)-1].split(',')
    last_address = last_account[0]
    last_private_key = last_account[1]
    response = {'account_number': len(accounts),
                    'last_address': last_address,
                    'last_private_key':last_private_key}
    return jsonify(response), 201
    
    
    

# Mining a new block
@app.route('/mine_block', methods = ['POST'])
def mine_block():
    json = request.get_json()
    account_keys=['address']
    is_valid=False
    if not all(key in json for key in account_keys):
        return 'Mine Issue, address is not valid', 400
    for i in range(len(accounts)):
        data = accounts[i].split(',')
        if json['address'] == data[0]:
            is_valid=True
    if is_valid == False:
        response = {'message':'Mine Issue, address is not valid!'}
        return jsonify(response),201
        
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender = node_address, receiver = json['address'], amount = '0.001')
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']}
    return jsonify(response), 201

# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': True}
    else:
        response = {'message': False}
    return jsonify(response), 200

# Adding a new transaction to the Blockchain
@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json for key in transaction_keys):
        return 'Some elements of the transaction are missing', 400
    
    
    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    response = {'message': f'This transaction will be added to Block {index}'}
    return jsonify(response), 201

# Part 3 - Decentralizing our Blockchain
 
# Connecting new nodes
@app.route('/connect_node', methods = ['POST'])   #We will use later
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return "No node", 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'All the nodes are now connected. The Prometheum Blockchain now contains the following nodes:',
                'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201

 

# Replacing the chain by the longest chain if needed
@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'The nodes had different chains so the chain was replaced by the longest one.',
                    'new_chain': blockchain.chain}
    else:
        response = {'message': 'All good. The chain is the largest one.',
                    'actual_chain': blockchain.chain}
    return jsonify(response), 200


@app.route('/get_all_miners', methods = ['GET'])
def get_all_miners():
     miners = []
     for i in range(len(blockchain.chain)):
         block = blockchain.chain[i]
         trans_data = block['transactions']
         for j in range(len(trans_data)):
             trans = trans_data[j]
             if trans['sender'] == 'f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0':
                 miners.append(trans['receiver'])
     response = {"miners":miners}
     return jsonify(response),200

@app.route('/get_all_mining_datetime', methods = ['GET'])
def get_all_mining_datetime():
    dates = []
    for i in range(len(blockchain.chain)):
        if i!=0:
            block = blockchain.chain[i]
            dates.append(block['timestamp'])
    response = {"timestamp":dates} 
    return jsonify(response),200


@app.route('/get_last_mining_time_from_address',methods = ['POST'])
def get_last_mining_time_from_address():
    json = request.get_json()
    address = json['address']
    time_stamp = "-1"
    for i in range(len(blockchain.chain)):
        block = blockchain.chain[i]
        for j in range(len(block['transactions'])):
            trans = block['transactions'][j]  
            if trans['sender'] == 'f0b6081f8b6f472b8d27ca04537e50c4d2a17d6f05fe466db0fbf89cfe1e51f0' and trans['receiver'] == address:
                time_stamp = block['timestamp']
                
    response = {"timestamp":time_stamp}
    return jsonify(response),201
                
                

# Running the app
app.run(host = '127.0.0.1', port = 5000)
 

 


