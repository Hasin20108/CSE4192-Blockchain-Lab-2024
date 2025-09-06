# Task 1: Version, Previous Hash, Merkle Root (Use a dummy merkle root), Timestamp , Difficulty, Nonce
# Task 2: Create a Blockchain 


import hashlib 
import json 

class Blockheader:
    def __init__(self, version, difficulty, previous_hash="0"):
        self.version = version  
        self.difficulty = difficulty
        self.previous_hash = previous_hash

class Block:
    def __init__(self, data, blockheader): 
        self.data = data 
        self.blockheader = blockheader 
        self.nonce = 0 
        self.hash = ""
        self.mine(self.blockheader.difficulty)

    def mine(self, difficulty): 
        while self.hash[0:difficulty] != '0' * difficulty:
            self.nonce += 1 
            hash_string = str(self.data)+str(self.blockheader.previous_hash)+str(self.nonce) + str(self.blockheader.version)
            self.hash = hashlib.sha256(hash_string.encode()).hexdigest()
            print(f"Mining... Nonce: {self.nonce}, Hash: {self.hash}", end='\r')

        return self.hash

    def serialize(self):
        block_dict = {
            "data": self.data,
            "blockheader": self.blockheader.__dict__,
            "nonce": self.nonce,
            "hash": self.hash
        }
        return json.dumps(block_dict)  # Pretty JSON format


blockheader = Blockheader(1, 4, "00000000000000000000000000")
block = Block("Block 1",blockheader) 

print(block.serialize())



