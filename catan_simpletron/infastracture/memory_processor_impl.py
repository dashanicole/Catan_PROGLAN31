from memory_domain.entities import Instruction, Address
from memory_domain.entities.processor import Processor
from memory_domain.dtos.read_data_dto import ReadDataDto
from memory_domain.repository.memory_repository import MemoryRepository
from memory_domain.repository.processor_repository import ProcessorRepository
from memory_domain.operations.operation_mapping import operation_mapping

class ProcessorRepositoryImpl(ProcessorRepository):  
    def __init__(self, processor: Processor, memory_repository: MemoryRepository):
        super().__init__(processor, memory_repository)
        self.operation_map = operation_mapping(self)

    def fetch(self):
        program_counter = int(self.processor.program_counter)
        address = f"0{program_counter}" if program_counter < 10 else f"{program_counter}"
        self.processor.instruction_register = self.memory_repository.read_data(dto=ReadDataDto(address=Address(address)))

    
    def decode(self) -> Instruction | None:
        instruction = self.processor.instruction_register
        if len(repr(instruction)) <= 0 or not instruction or isinstance(instruction, str):
            return None; 

        self.processor.operation_code = instruction.operator_code
        self.processor.operand = instruction.operand  
        return Instruction(self.processor.instruction_register)
    
    def execute(self, instruction: Instruction) -> bool:
        if self.processor.operation_code == "43":  
            return True  

        if self.processor.operation_code in self.operation_map:
            self.operation_map[self.processor.operation_code](instruction.operand)  
            
        else: 
            raise ValueError(f"Unknown opcode: {self.processor.operation_code}...")
        
        return False  
    
    def dump(self) -> str | None:
        return self.processor.dump()
        
    

        