from core.base.core_dto import CoreDto
from core.error.memory_error import MemoryError
from memory_domain.entities import Address, DataValue, Instruction

class StoreDataDto(CoreDto):
    def __init__(self, address: Address, data: DataValue | Instruction) -> None:
        self.address = address
        self.data = data 
        self.validate()
        
    def validate(self) -> None:
        errors = []

        if not self.address:
            errors.append('Address is required')

        if not self.data:
            errors.append('DataValue is required')

        if errors:
            raise MemoryError.validation_errors("Error creating store data dto", errors)