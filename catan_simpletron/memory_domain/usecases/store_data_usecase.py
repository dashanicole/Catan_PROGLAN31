from memory_domain.dtos import StoreDataDto
from memory_domain.repository.memory_repository import MemoryRepository

class StoreData:
    def __init__(self, repository: MemoryRepository):
        self.repository = repository

    def execute(self, dto: StoreDataDto) -> bool:
        return self.repository.store_data(dto)