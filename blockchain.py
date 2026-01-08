import hashlib

class Block:
    def __init__(self, data, prev, hash):
        self.data = data
        self.prev = prev
        self.hash = hash
        
class Blockchain:
    def __init__(self):
        data = 'block-1'
        prev = hashlib.sha256(('start-from').encode()).hexdigest()
        curr = hashlib.sha256((data + prev).encode()).hexdigest()
        block = Block(data, prev, curr)
        
        self.chain = [block]
    
    def add_block(self, data):
        prev = self.chain[-1].hash
        hash = hashlib.sha256((data + prev).encode()).hexdigest()
        new_block = Block(data, prev, hash)
        self.chain.append(new_block)
        print(f"block {new_block.hash} added!")
    
    def view_chain(self):
        first_end = hashlib.sha256(('start-from').encode()).hexdigest()
        start = self.chain[-1]
        while(start.prev != first_end):
            print(f"Hash: {start.hash} | Prev: {start.prev} | Data: {start.data}")
            start = [block for block in self.chain if block.hash == start.prev][0]
    
    def write_on_block(self, id, data):
        # immutability
        target = self.chain[id]
        target.data = data
        target.hash = hashlib.sha256((data + target.prev).encode()).hexdigest()
        new_prev_hash = target.hash
        
        for i in range (id + 1, len(self.chain)):
            self.chain[i].prev = new_prev_hash
            self.chain[i].hash = hashlib.sha256((self.chain[i].prev + self.chain[i].data).encode()).hexdigest()
            new_prev_hash = self.chain[i].hash
        
        
    
    
my_chain = Blockchain()
a = int(input("1. View chain, 2. Write on block, 3. Add new block"))
while(a != 4):
    if a == 1:
        my_chain.view_chain()
    elif a == 2:
        data = input("Data to write: ")
        id = int(input("Where to write: "))
        my_chain.write_on_block(data=data, id=id)
        
    elif a == 3:
        data = input("Data to store: ")
        my_chain.add_block(data=data)
    else:
        break
    
    a = int(input("1. View chain, 2. Write on block, 3. Add new block"))
    