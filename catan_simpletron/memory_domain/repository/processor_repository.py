from abc import ABC, abstractmethod
from memory_domain.entities.instruction_entity import Instruction
from memory_domain.entities.processor import Processor
from memory_domain.repository.memory_repository import MemoryRepository

class ProcessorRepository(ABC):
    def __init__(self, processor: Processor, memory_repository: MemoryRepository):
        self.processor = processor
        self.memory_repository = memory_repository

    @abstractmethod
    def fetch(self): pass
    
    @abstractmethod
    def decode(self) -> Instruction: pass
     
    @abstractmethod
    def execute(self, instruction: Instruction) -> None: pass

    @abstractmethod
    def dump() -> str | None: pass