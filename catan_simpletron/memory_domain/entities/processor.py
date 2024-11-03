from .instruction_entity import Instruction

class Processor:
    def __init__(self):
        self._accumulator = 0
        self._program_counter = 0
        self._instruction_register: Instruction = Instruction("0000")  
        self._operation_code = 0
        self._operand = 0

    @property 
    def accumulator(self): 
        return self._accumulator

    @accumulator.setter
    def accumulator(self, new_value):
        self._accumulator = new_value

    @property
    def program_counter(self):
        return self._program_counter

    @program_counter.setter
    def program_counter(self, new_value):
        self._program_counter = new_value

    @property
    def instruction_register(self):
        return self._instruction_register

    @instruction_register.setter
    def instruction_register(self, new_value):
        self._instruction_register = new_value

    @property
    def operation_code(self):
        return self._operation_code

    @operation_code.setter
    def operation_code(self, new_value):
        self._operation_code = new_value

    @property
    def operand(self):
        return self._operand

    @operand.setter
    def operand(self, new_value):
        self._operand = new_value

    def increment_program_counter(self):
        self.program_counter += 1

    def dump(self) -> str:
        """Dumps the current state of the processor as a string."""
        state = {
            "Accumulator": f"+{str(self.accumulator).zfill(4)}",
            "Program Counter": f"0{self.program_counter}",
            "Instruction Register": f"+{self.instruction_register}",
            "Operation Code": self.operation_code,
            "Operand": self.operand,
        }

        output = "\nREGISTERS:\n"  
        
        max_key_length = max((len(key) for key in state)) + 7

        for key, value in state.items():
            output += f"{key}: {value:>{max_key_length - len(key)}}\n" 
        
        return output  
