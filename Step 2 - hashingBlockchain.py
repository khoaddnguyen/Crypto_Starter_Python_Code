import hashlib

class Block:
    def __init__(self,data):
        self.data = data
        self.prev_hash = ""
        self.hash = ""

def hash(block):
    data = block.data + block.prev_hash
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

        self.chain.append(block)

    def print(self):
        for block in self.chain:
            print("")
            print("Data: ", block.data)
            print("Previous hash:", block.prev_hash)
            print("Hash: ", block.hash)
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

blockchain.chain[1].data = "Changing Block #1"
#Changing previous hash to bypass is_valid test
blockchain.chain[1].hash = hash(blockchain.chain[1])

blockchain.print()
print("Is_valid?: ", blockchain.is_valid())
