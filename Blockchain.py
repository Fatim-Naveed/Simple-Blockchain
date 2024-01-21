import hashlib
import time

class Block:
    static_index=1
  
    def __init__(self,data,previous_hash):
        self.Block_index=Block.static_index
        self.Transaction_List=data
        self.previous_hash=previous_hash
        self.timestamp = time.time()
        self.hash=None
        self.prev=None
        self.nonce=None
        Block.static_index+=1

#====================================================================================
class blockchain:
    
    LastHash="0"
    MiningDifficulty=2
    NonceLimit=1000000
    
    def __init__(self):
        self.head=None

    def HashingFunction(self,block):
        self.hash_string=str(block.Block_index)+"-"+str(block.Transaction_List)+"-"+block.previous_hash+"-"+str(block.timestamp)
        self.HashValue=hashlib.sha256(self.hash_string.encode())
        self.HashValue=self.HashValue.hexdigest()
        blockchain.LastHash=self.HashValue
        block.hash=self.HashValue
        
#====================================================================================
    def AddNewBlock(self):
        
        sender=input("Enter sender : ")
        reciever=input("Enter Reciever : ")
        amount=float(input("Enter amount : "))
        Transaction=f"{sender} gave {reciever} {amount} dollars"
        
        New_block=Block(Transaction,blockchain.LastHash)
    
        if(blockchain.LastHash != New_block.previous_hash ):
            print("Faulty Block deteced !")
            return
        
        self.HashingFunction(New_block)
        self.mine(New_block)
        
        
        New_block.prev=self.head
        self.head = New_block    
#====================================================================================
        
    def mine(self,block):
        for nonce in range(blockchain.NonceLimit):
            hash_string=str(block.Block_index)+"-"+str(block.Transaction_List)+"-"+block.previous_hash+"-"+str(block.timestamp)+str(nonce)
            hash_try=hashlib.sha256(hash_string.encode()).hexdigest()
            if hash_try.startswith('0'*blockchain.MiningDifficulty):
                print(f"found nonce : {nonce}")
                block.nonce=nonce
                return
    
#====================================================================================
    def PrintBlockChain(self):
        print("\n Blockchain : \n")
        currenthash=self.head
        while(currenthash.previous_hash!="0"):
            print(f"Block Index-> {currenthash.Block_index}")
            print(f"Transaction-> {currenthash.Transaction_List}")
            print(f"Nonce-> {currenthash.nonce}")
            print(f"This Hash-> {currenthash.hash}")
            print(f"Prev Hash-> {currenthash.previous_hash}\n")
            if(currenthash.previous_hash!=currenthash.prev.hash):
               print("faulty")
               return
            currenthash=currenthash.prev
    
        print(f"Block Index-> {currenthash.Block_index}")
        print(f"Transaction-> {currenthash.Transaction_List}")
        print(f"Nonce-> {currenthash.nonce}")
        print(f"This Hash-> {currenthash.hash}")
        print(f"Genisis Block Reached -> {currenthash.previous_hash}")
#====================================================================================
GenisisBlock=blockchain()
GenisisBlock.AddNewBlock()
GenisisBlock.AddNewBlock()
GenisisBlock.AddNewBlock()
# GenisisBlock.AddNewBlock()
GenisisBlock.PrintBlockChain()

