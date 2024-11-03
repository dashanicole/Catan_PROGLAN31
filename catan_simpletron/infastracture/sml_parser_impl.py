from core.base.sml_parser import ISMLParser
from presentation.memory_controller import MemoryController

class SMLParserImpl(ISMLParser):
    """
        Parses the SML file and loads instructions/data into memory.
    """
    @staticmethod
    def parse_and_load_sml(filename: str, controller: MemoryController) -> None:
        with open(filename, 'r') as file:
            for line in file:
                # Strip line of any leading/trailing spaces
                line = line.strip()

                # Skip empty lines or comments only lines
                if not line or line.startswith(';'):
                    continue

                # Split parts into three components (Address, Instruction/Data, and Comment) 
                parts = line.split()

                if len(parts) < 2:
                    continue  # Invalid line, skip

                raw_address = parts[0]
                raw_instruction_data_str = parts[1]  

                # Controller automatically checks if the value is a (Instruction/DataValue)
                controller.store(raw_address, raw_instruction_data_str)
