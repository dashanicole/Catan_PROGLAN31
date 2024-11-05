from core.base.sml_parser import ISMLParser
from infastracture.mnemonic_parser_impl import MnemonicAssigner
from presentation.memory_controller import MemoryController
from memory_domain.operations.mnemonic_mapping import MNEMONIC


class SMLParserImpl(ISMLParser):
    mnemonic_parser = MnemonicAssigner()

    """
        Parses the SML file with mnemonics and loads instructions/data into memory.
    """
    def parse_and_load_sml(cls, filename: str, controller: MemoryController) -> None:
        address_counter = 0 
        address_assigner = cls.mnemonic_parser.parse_sml_mnemonics(filename)

        print(f"\n\n{address_assigner}")
      
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith(';'):
                    continue
                
                parts = line.split()

                # Extract mnemonic and argument
                mnemonic = parts[0]
                argument = parts[1]

                # map argument
                if argument in address_assigner:
                    argument = address_assigner[argument]

                # Map mnemonic to opcode
                opcode = MNEMONIC.get(mnemonic)
                if opcode is None:
                    raise ValueError(f"Unrecognized mnemonic: {mnemonic}")

                # Format instruction: combine opcode with argument
                if mnemonic != "Halt":
                    argument = str(int(argument)).zfill(2) 
                    instruction = f"{opcode:02}{argument}"  # Combine opcode and argument
                else:
                    instruction = f"{43}00"  

                # Convert address counter to a two-digit address format
                address = f"{address_counter:02}"

                # Store in memory using the address and formatted instruction
                controller.store(address, instruction)

                # Increment the address counter for the next instruction
                address_counter += 1