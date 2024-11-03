from abc import ABC, abstractmethod
from memory_domain.dtos import StoreDataDto, ReadDataDto 
from memory_domain.entities import DataValue

class MemoryRepository(ABC): 
    @abstractmethod
    def store_data(dto: StoreDataDto) -> bool: pass

    @abstractmethod
    def read_data(dto: ReadDataDto) -> DataValue: pass

    @abstractmethod
    def dump(self) -> str: pass