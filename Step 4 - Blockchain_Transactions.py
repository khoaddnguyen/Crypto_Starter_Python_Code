import hashlib, json
from datetime import datetime, timedelta

class Block:
    def __init__(self,data):
        self.data = data
        self.prev_hash = ""
        self.nonce = 0
        self.hash = ""
        self.total_time = 0

def hash(block):
    #turn dict to JSON
    data = json.dumps(block.data) + block.prev_hash + str(block.nonce)
    data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()



class Blockchain:
    #Genesis Block
    def __init__(self):
        self.chain = []
        
        block = Block("Genesis Block")
        block.hash = hash(block)

        self.chain.append(block)

    #Add next block
    def add_block(self, data):
        block = Block(data)
        block.prev_hash = self.chain[-1].hash
        block.hash = hash(block)
        start = datetime.now()
        while hash(block).startswith("00") == False:
            block.nonce = block.nonce + 1
            block.hash = hash(block)
        end = datetime.now()
        block.total_time = str(end - start)

        self.chain.append(block)

    def print(self):
        for block in self.chain:
            print("")
            print("Data: ", block.data)
            print("Previous hash:", block.prev_hash)
            print("Hash: ", block.hash)
            print("Nonce: ", block.nonce)
            print("total time: ", block.total_time)
            print("")

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            if hash(current_block) != current_block.hash:
                return False
            
            #enhanced is_valid test
            if prev_block.hash != current_block.prev_hash:
                return False
            
        return True

    #adding blocks will not save each person's balances
    # the get_balance() function goes through the history of the entire blockchain to track the balances
    # to simplify, the IF statement was inserted to filter for the list[] data type only
    def get_balance(self, person):
        balance = 0
        for block in self.chain:
            if type(block.data) != list:
                continue
            for transfer in block.data:
                if transfer["from"] == person:
                    balance = balance - transfer["amount"]
                if transfer["to"] == person:
                    balance = balance + transfer["amount"]
        return balance
    
blockchain = Blockchain()
#adding data in a form of banking transactions
blockchain.add_block([
    {"from": "Britney Spears", "to": "Spiderman", "amount": 1000},
    {"from": "Lady Gaga", "to": "Captain America", "amount": 20000},
    {"from": "Taylor Swift", "to": "Aquaman", "amount": 400000},
    ])

blockchain.add_block([
    {"from": "Lady Gaga", "to": "Aquaman", "amount": 7500},
    {"from": "Taylor Swift", "to": "Spiderman", "amount": 490},
    {"from": "Lady Gaga", "to": "Britney Spears", "amount": 8000},
    ])



#print("Is_valid?: ", blockchain.is_valid())

print("Balance of Spiderman:", blockchain.get_balance("Spiderman"), "USD")
blockchain.print()
