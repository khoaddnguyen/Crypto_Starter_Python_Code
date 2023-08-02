import hashlib
from datetime import datetime, timedelta

class Block:
    def __init__(self,data):
        self.data = data
        self.prev_hash = ""
        self.nonce = 0
        self.hash = ""
        self.total_time = 0

def hash(block):
    data = block.data + block.prev_hash + str(block.nonce)
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
        while hash(block).startswith("00000") == False:
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

blockchain = Blockchain()
blockchain.add_block("This is test #2")
blockchain.add_block("This is test #3")
blockchain.add_block("This is test #4")

'''
#This is hacker's attempts to change a block in a chain

blockchain.chain[1].data = "Changing Block #1"
#Changing previous hash to bypass is_valid test
blockchain.chain[1].hash = hash(blockchain.chain[1])

blockchain.chain[2].prev_hash = blockchain.chain[1].hash
blockchain.chain[2].hash = hash(blockchain.chain[2])

blockchain.chain[3].prev_hash = blockchain.chain[2].hash
blockchain.chain[3].hash = hash(blockchain.chain[3])
'''


print("Is_valid?: ", blockchain.is_valid())
blockchain.print()
