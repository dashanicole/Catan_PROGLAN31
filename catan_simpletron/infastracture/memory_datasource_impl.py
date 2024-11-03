from typing import Union
from memory_domain.datasource.memory_datasource import MemoryDatasource
from memory_domain.entities.memory import Memory
from memory_domain.dtos import ReadDataDto, StoreDataDto
from memory_domain.entities import DataValue, Instruction

class MemoryDatasourceImpl(MemoryDatasource):
    def __init__(self, memory: Memory) -> None:
        self.memory = memory 
       
    def store_data(self, dto: StoreDataDto) -> bool:
        return self.memory.store(
                                dto.address,
                                dto.data)

    def read_data(self, dto: ReadDataDto) -> Union[Instruction, DataValue]:
        return self.memory.read(dto.address)

    def dump(self) -> None: 
        return self.memory.show()





    