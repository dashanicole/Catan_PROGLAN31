from typing import Type
from core.error.memory_error import MemoryError;
from core.base.core_entity import CoreEntity;

"""
    Represents an address in memory.
"""
class Address(CoreEntity): 
    def __init__(self, value: str) -> None:
        value = str(value)
        super().__init__(value) 
        self.value = value;
        if not self.is_valid(value):
            raise MemoryError.invalid_address("Invalid address...")
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Address):
            return self.value == other.value
        return False
    
    def __hash__(self) -> int:
        return hash(self.value)

    def is_valid(self, value: str) -> bool:
        return len(value) == 2 and value.isdigit();

    @property
    def get_memory_address(self) -> Type['Address']: 
        return Address(f'{self.value[0]}0')

    @property
    def get_col_location(self) -> int:
        return int(self.value[1])

    
    

    