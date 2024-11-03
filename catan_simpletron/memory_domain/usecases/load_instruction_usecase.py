from core.base.sml_parser import ISMLParser
from presentation.memory_controller import MemoryController

class LoadInstruction:
    def __init__(self, parser: ISMLParser):
        self.parser = parser
    
    def execute(self, filename: str, controller: MemoryController) -> None:
        return self.parser.parse_and_load_sml(filename, controller)