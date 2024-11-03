from abc import ABC, abstractmethod
from presentation.memory_controller import MemoryController

class ISMLParser(ABC): 
    @abstractmethod
    def parse_and_load_sml(filename: str, controller: MemoryController) -> None: pass