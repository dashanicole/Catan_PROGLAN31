from typing import List, Type
from core.constants.memory_error_types import MemoryErrorType

class MemoryError(Exception):
    def __init__(self, message: str, error_type: MemoryErrorType = MemoryErrorType.GENERAL):
        super().__init__(message);
        self.error_type = error_type; 

    def __str__(self):
        return f"error_type: [{self.error_type.name}]\nmessage: {super().__str__()}"

    @staticmethod
    def invalid_address(message: str) -> Type['MemoryError']:
        return MemoryError(message, error_type=MemoryErrorType.INVALID_ADDRESS)
    
    @staticmethod
    def memory_overflow() -> Type['MemoryError']:
        return MemoryError("Memory overflow. Cannot store more data", error_type=MemoryErrorType.MEMORY_OVERFLOW)
    
    @staticmethod
    def memory_access_error(raw_address: str) -> Type['MemoryError']:
        return MemoryError(f"Cannot access memory at address: {raw_address}", error_type=MemoryErrorType.MEMORY_ACCESS)
    

    @staticmethod
    def invalid_data(message: str) -> Type['MemoryError']:
        return MemoryError(message, error_type=MemoryErrorType.INVALID_DATA)
    
    @staticmethod
    def invalid_instruction(message: str) -> Type['MemoryError']:
        return MemoryError(message, error_type=MemoryErrorType.INVALID_INSTRUCTION)

    @staticmethod
    def data_not_found(raw_address: str) -> Type['MemoryError']:
        return MemoryError(f"No data found at address: {raw_address}", error_type=MemoryErrorType.DATA_NOT_FOUND)
    
    @classmethod 
    def validation_errors(cls, message: str, errors: List[str] | str) -> Type['MemoryError']:
        error_data = ', '.join(errors) if type(errors) == List[str]  else ''.join(errors)
        return cls(f"{message}\nerrors: {error_data}", error_type=MemoryErrorType.VALIDATION_ERROR)