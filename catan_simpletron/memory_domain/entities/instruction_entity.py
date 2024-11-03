from core.base.core_entity import CoreEntity
from core.error.memory_error import MemoryError

class Instruction(CoreEntity): 
    def __init__(self, value: str) -> None:
        value = str(value)
        super().__init__(value) 
        self.value = value 

        # if not self.is_valid(self.value):
        #     raise MemoryError.invalid_instruction('Invalid instruction')

    def is_valid(self, value: str) -> bool:
        return len(value) == 4
    
    @property
    def operator_code(self) -> str:
        return self.value[0:2]
    
    @property
    def operand(self) -> str:
        return self.value[2:4]