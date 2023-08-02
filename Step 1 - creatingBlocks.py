import hashlib

class Block:
    def __init__(self,data):
        #hash algo. sha256 aka 256 bits or 32 bytes
        self.data = data
        self.hash = ""

def hash(block):
    data = block.data
    data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()
    
#block = Block("This is a test")
#print(hash(block))


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
        block.hash = hash(block)

        self.chain.append(block)

    def print(self):
        for block in self.chain:
            print("Data: ", block.data)
            print("Hash: ", block.hash)
        print()

blockchain = Blockchain()
blockchain.add_block("This is test #2")
blockchain.add_block("This is test #3")
blockchain.add_block("This is test #4")

blockchain.print()
