from core.base.core_dto import CoreDto
from core.error.memory_error import MemoryError
from memory_domain.entities import Address

class ReadDataDto(CoreDto):
    def __init__(self, address: Address) -> None:
        self.address = address
        self.validate()

    def validate(self) -> None:
        if not self.address:
            raise MemoryError.validation_errors('Failed create read data dto', 'Address is required');
    