'''
	Simpletron memory
'''
from os import system,sys,path

class Memory(object):
    def __init__(self,size:int):
        self.memory:list = []
        self.size = size
        self.count = 0
        for i in range(0,self.size):
            self.memory.append('0000')
        
    def getitem(self,address:int)->str:
        return self.memory[address]
        
    def setitem(self,address:int,value:str)->None:
        self.memory[address] = value
        
    def __str__(self)->str:
        return str(self.memory)

def dump(mem:list)->None:
    
    dcount:int = 1
    [print(f"{i:8}",end="") for i in range(0,10)]
    print(f"\n00",end=" ")
    for i in range(0,len(mem)):
        if dcount % 10 == 0 and dcount<100:
            print(f"+{mem[i]:7}")
            print(f"{(i+1)}",end=" ")
        else:
            print(f"+{mem[i]:7}",end="")
        dcount+=1
    print()
    print('-'*100)
    
def loader(filename:str)->None:
    program:list = []
    if path.exists(filename):
        file = open(filename)
        program = file.readlines()
        file.close()
    return program
        
    
def main()->None:
    # filename:str = "add.sml"
    m = Memory(100)
    # system('cls')
    filename:str = str(sys.argv[1])
    # print(filename)
    program:list = loader(filename)
    
    for item in program:
        instruction:list = item.strip().split("\t")
        
        address = instruction[0]
        command = instruction[1]
        m.setitem(int(address),command)
        
    dump(m.memory)
    
if __name__=="__main__":
    main()
    
    