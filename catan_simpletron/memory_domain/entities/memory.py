from typing import Dict, List, Union
from memory_domain.entities import Address, Instruction, DataValue
from core.error.memory_error import MemoryError

class Memory:
    memory: Dict[Address, List[Union[Instruction, DataValue, str]]] = {} 

    @classmethod
    def initialize_memory(cls, num_locations: int) -> None:
        cls.memory = {Address(f'{i}0'): [] for i in range(num_locations)}
        for key in cls.memory:
            for _ in range(len(cls.memory)):
                cls.memory[key].append('0000')

    @classmethod
    def store(cls, address: Address, data: Union[Instruction, DataValue]) -> bool:
        in_memory_address = address.get_memory_address
        if in_memory_address not in cls.memory:
            raise MemoryError.invalid_address(f"Invalid address in memory: {address}")

        location = address.get_col_location
        if location >= len(cls.memory[in_memory_address]):
            raise MemoryError.memory_overflow()

        if isinstance(data, Instruction):
            cls.memory[in_memory_address][location] = Instruction(data)
        elif isinstance(data, DataValue):
            cls.memory[in_memory_address][location] = DataValue(data)
        else:
            raise MemoryError.invalid_data("Data must be Instruction or DataValue")

        return True
    
    @classmethod
    def read(cls, address: Address) -> DataValue: 
        in_memory_address = address.get_memory_address
        if in_memory_address not in cls.memory:
            raise MemoryError.invalid_address('Address is not present in the memory')

        location = address.get_col_location
        if location >= len(cls.memory[in_memory_address]):
            raise MemoryError.memory_access_error(str(in_memory_address))
        
        return cls.memory[in_memory_address][location]
    

    @classmethod
    def show(cls) -> str:
        output = ""
        
        first_key = next(iter(cls.memory))  
        row_length = len(cls.memory[first_key]) 
    
        for index in range(row_length):
            output += f'{index:>11}'  
        output += '\n'  

        for key in cls.memory:
            output += f'{key:>2} '  
            for loc in cls.memory[key]:
                if isinstance(loc, (Instruction, DataValue)):
                    content = f'+{str(loc).zfill(4)}' 
                else:
                    content = f'+{loc.zfill(4)}'  
                output += f'{content:>10} '  
            output += '\n'  
        
        return output  


