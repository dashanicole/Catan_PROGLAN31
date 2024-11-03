from memory_domain.dtos import ReadDataDto
from memory_domain.repository.memory_repository import MemoryRepository
from memory_domain.entities import DataValue

class ReadData:
    def __init__(self, repository: MemoryRepository):
        self.repository = repository

    def execute(self, dto: ReadDataDto) -> DataValue:
        return self.repository.read_data(dto)