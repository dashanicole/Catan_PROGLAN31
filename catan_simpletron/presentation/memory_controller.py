from memory_domain.repository.memory_repository import MemoryRepository
from memory_domain.usecases.store_data_usecase import StoreData
from memory_domain.usecases.read_data_usecase import ReadData
from core.error.memory_error import MemoryError
from memory_domain.dtos import StoreDataDto, ReadDataDto
from memory_domain.entities import Address, DataValue, Instruction
  
class MemoryController: 
    def __init__(self, repository: MemoryRepository):
        self.repository = repository

    """
        Controller method to store data in memory.
        @param raw_address: The raw address where data should be stored.
        @param raw_data: The raw data to be stored in memory.
        @return: bool indicating success or failure.
    """
    def store(self, raw_address: str, raw_data_or_instruction: str | DataValue | Instruction) -> bool:
        try:
            # Convert raw_address to Address object
            address = Address(raw_address)
            
            # Depending on the data format, parse it as Instruction or DataValue
            if raw_data_or_instruction == '0000' or isinstance(raw_data_or_instruction, DataValue):
                data = DataValue(raw_data_or_instruction)
            else:
                data = Instruction(raw_data_or_instruction)
            
            # Create DTO to pass to the use case
            store_dto = StoreDataDto(address, data)

            # Execute the use case to store in memory
            store_use_case = StoreData(self.repository)
            return store_use_case.execute(store_dto)
        
        except MemoryError as e:
            print(f"Memory Error: {str(e)}...")
            return False

    """
        Controller method to read data in memory.
        @param raw_address: The raw address from which to read data.
        @return: DataValue if successful, None if an error occurs.
    """
    def read(self, raw_address: str) -> DataValue:
        try:
            read_dto = ReadDataDto(address=Address(raw_address))
            read_use_case = ReadData(self.repository)
            return read_use_case.execute(read_dto)
        except MemoryError as e:
            print(f"\n{str(e)}") 

    """
        Controller method display the current state of the memory.
        @return: None
    """
    def display(self) -> str:
        return self.repository.dump()