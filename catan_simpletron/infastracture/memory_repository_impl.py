from memory_domain.dtos import StoreDataDto, ReadDataDto
from memory_domain.entities import DataValue
from memory_domain.repository.memory_repository import MemoryRepository
from memory_domain.datasource.memory_datasource import MemoryDatasource

class MemoryRepositoryImpl(MemoryRepository):
    def __init__(self, datasource: MemoryDatasource):
        self.datasource = datasource

    def store_data(self, dto: StoreDataDto) -> bool:
        return self.datasource.store_data(dto)

    def read_data(self, dto: ReadDataDto) -> DataValue:
        return self.datasource.read_data(dto)
    
    def dump(self) -> None:
        return self.datasource.dump()