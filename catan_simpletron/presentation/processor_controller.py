from memory_domain.repository.memory_repository import MemoryRepository
from memory_domain.repository.processor_repository import ProcessorRepository
from memory_domain.operations.operation_mapping import operation_mapping
from .cli_utils import wrap_in_border

class ProcessorController:  
    dump = ["ReadA", "LoadI", "Store", "LoadM", "JZ", "HALT", "Store", "MulM", "Store", "LoadM", "SubI", "Store", "JMP", "Write", "VariableA", "VariableB"]
    counter = 0;

    def __init__(self, processor_repository: ProcessorRepository, memory_repository: MemoryRepository):
        self.processor_repository = processor_repository
        self.memory_repository = memory_repository
        self.operation_map = operation_mapping(self)

    def run_single_step(self):
        while True: 
            self.processor_repository.fetch()
            instruction = self.processor_repository.decode()

            if not instruction:
                print("Program terminated normally...\n")
                break

            should_halt = self.processor_repository.execute(instruction)  

            if should_halt:
                print("Program terminated normally...\n")
                break 

    def run_step_by_step(self): 
        flag = 0

        while True: 
            dump_output = self.processor_repository.dump()
            memory_output = self.memory_repository.dump()
            wrap_in_border(dump_output, memory_output)

            if flag != 0:
                print("\nPress any key to continue...")    
                input()
            else:
                print("\nPress any key to start execution...")    
                input()
            
            self.processor_repository.fetch()
            instruction = self.processor_repository.decode()

            if not instruction:
                break;

            # print(f"\nExecuting {str(instruction)}")

            print(f"\nExecuting {self.dump[self.counter]}")
            self.counter += 1;

            should_halt = self.processor_repository.execute(instruction)  

            flag += 1

            if should_halt:
                print("Program terminated normally...\n")
                self.processor_repository.processor.increment_program_counter()
                dump_output = self.processor_repository.dump()
                memory_output = self.memory_repository.dump()
                wrap_in_border(dump_output, memory_output)
                break


            
        

            