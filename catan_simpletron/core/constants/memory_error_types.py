from enum import Enum;

class MemoryErrorType(Enum): 
    INVALID_ADDRESS = "InvalidAdressError"
    MEMORY_OVERFLOW = "MemoryOverflowError"
    MEMORY_ACCESS = "MemoryAccessError"
    DATA_NOT_FOUND = "DataNotFoundError"
    INVALID_DATA = "InvalidDataError"
    INVALID_INSTRUCTION = "InvalidInstructionError"
    VALIDATION_ERROR = "ValidationError"
    GENERAL = "MemoryError" 