from memory_domain.entities import Address, DataValue
from memory_domain.dtos import StoreDataDto, ReadDataDto
from memory_domain.repository.processor_repository import ProcessorRepository
from memory_domain.usecases import StoreData, ReadData  


class ProcessorOperations:
    def __init__(self, processor_repository: ProcessorRepository, show_steps=False):
        self.processor_repository = processor_repository
        self.show_steps = show_steps

    def read(self, address: str):
        """Reads input into the memory address."""
        if self.show_steps:
            print(f"Note: Get a value from user input and store it at address {str(address).zfill(2)}.")
        value = input("? ")   
        StoreData(self.processor_repository.memory_repository).execute(self.create_store_dto(address, value))
        self.processor_repository.processor.increment_program_counter()

    def write(self, address: str):
        """Writes the content of the memory address to output."""
        if self.show_steps:
            print(f"Note: Output the content stored at address {str(address).zfill(2)}.")
        read_dto = self.create_read_dto(address)
        value = repr(ReadData(self.processor_repository.memory_repository).execute(read_dto))
        print(f"> {value}\n")
        self.processor_repository.processor.increment_program_counter()

    def load_m(self, address: str):
        """Loads the value from memory into the accumulator."""
        if self.show_steps:
            print(f"Note: Load the value at address {str(address).zfill(2)} into the accumulator.")
        read_dto = self.create_read_dto(address)
        self.processor_repository.processor.accumulator = int(repr(ReadData(self.processor_repository.memory_repository).execute(read_dto)))
        self.processor_repository.processor.increment_program_counter()

    def store_m(self, address: str):
        """Stores the accumulator's value into memory."""
        if self.show_steps:
            print(f"Note: Store the accumulator's value to address {str(address).zfill(2)}.")
        store_dto = self.create_store_dto(address, str(self.processor_repository.processor.accumulator))
        StoreData(self.processor_repository.memory_repository).execute(store_dto)
        self.processor_repository.processor.increment_program_counter()

    def load_i(self, operand: str):  
        """Load an immediate value into the accumulator."""
        if self.show_steps:
            print(f"Note: Load immediate value {operand} into the accumulator.")
        self.processor_repository.processor.accumulator = int(operand)
        self.processor_repository.processor.increment_program_counter()

    def add_m(self, address: str):
        """Adds the value from memory to the accumulator."""
        if self.show_steps:
            print(f"Note: Add the value at address {str(address).zfill(2)} to the accumulator.")
        read_dto = self.create_read_dto(address)
        val = int(repr(ReadData(self.processor_repository.memory_repository).execute(read_dto)))
        self.processor_repository.processor.accumulator += val
        self.processor_repository.processor.increment_program_counter()

    def sub_m(self, address: str):
        """Subtracts the value from memory from the accumulator."""
        if self.show_steps:
            print(f"Note: Subtract the value at address {str(address).zfill(2)} from the accumulator.")
        read_dto = self.create_read_dto(address)
        self.processor_repository.processor.accumulator -= int(repr(ReadData(self.processor_repository.memory_repository).execute(read_dto)))
        self.processor_repository.processor.increment_program_counter()

    def div_m(self, address: str):
        """Divides the accumulator by the value from memory."""
        if self.show_steps:
            print(f"Note: Divide the accumulator by the value at address {str(address).zfill(2)}.")
        read_dto = self.create_read_dto(address)
        value = int(repr(ReadData(self.processor_repository.memory_repository).execute(read_dto)))
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero...")
        self.processor_repository.processor.accumulator //= value
        self.processor_repository.processor.increment_program_counter()

    def mod_m(self, address: str):
        """Performs modulo division of the accumulator by the value from memory."""
        if self.show_steps:
            print(f"Note: Perform modulo division of the accumulator by the value at address {str(address).zfill(2)}.")
        read_dto = self.create_read_dto(address)
        value = int(repr(ReadData(self.processor_repository.memory_repository).execute(read_dto)))
        if value == 0:
            raise ZeroDivisionError("Cannot perform modulo division by zero...")
        self.processor_repository.processor.accumulator %= value
        self.processor_repository.processor.increment_program_counter()

    def mul_m(self, address: str):
        """Multiplies the accumulator by the value from memory."""
        if self.show_steps:
            print(f"Note: Multiply the accumulator by the value at address {str(address).zfill(2)}.")
        read_dto = self.create_read_dto(address)
        self.processor_repository.processor.accumulator *= int(repr(ReadData(self.processor_repository.memory_repository).execute(read_dto)))
        self.processor_repository.processor.increment_program_counter()

    def add_i(self, operand: str):
        """Adds an immediate operand to the accumulator."""
        if self.show_steps:
            print(f"Note: Add immediate operand {operand} to the accumulator.")
        self.processor_repository.processor.accumulator += int(operand)
        self.processor_repository.processor.increment_program_counter()

    def sub_i(self, operand: str):
        """Subtracts an immediate operand from the accumulator."""
        if self.show_steps:
            print(f"Note: Subtract immediate operand {operand} from the accumulator.")
        self.processor_repository.processor.accumulator -= int(operand)
        self.processor_repository.processor.increment_program_counter()

    def mod_i(self, operand: str):
        """Performs modulo division of the accumulator by an immediate operand."""
        if self.show_steps:
            print(f"Note: Perform modulo division of the accumulator by immediate operand {operand}.")
        operand = int(operand)
        if operand == 0:
            raise ZeroDivisionError("Cannot perform modulo division by zero...")
        self.processor_repository.processor.accumulator %= operand
        self.processor_repository.processor.increment_program_counter()

    def div_i(self, operand: str):
        """Divides the accumulator by an immediate operand."""
        if self.show_steps:
            print(f"Note: Divide the accumulator by immediate operand {operand}.")
        operand = int(operand)
        if operand == 0:
            raise ZeroDivisionError("Cannot divide by zero...")
        self.processor_repository.processor.accumulator //= operand
        self.processor_repository.processor.increment_program_counter()

    def mul_i(self, operand: str):
        """Multiplies the accumulator by an immediate operand."""
        if self.show_steps:
            print(f"Note: Multiply the accumulator by immediate operand {operand}.")
        self.processor_repository.processor.accumulator *= int(operand)
        self.processor_repository.processor.increment_program_counter()

    def jump(self, address: str):
        """Jumps to a specific memory address."""
        if self.show_steps:
            print(f"Note: Jump to memory address {str(address).zfill(2)}.")
        self.processor_repository.processor.program_counter = int(address)

    def jump_if_negative(self, address: str):
        """Jumps to a specific address if the accumulator is negative."""
        if self.show_steps:
            print(f"Note: Jump to address {str(address).zfill(2)} if the accumulator is negative.")
        if self.processor_repository.processor.accumulator < 0:
            self.processor_repository.processor.program_counter = int(address)
        else:
            self.processor_repository.processor.increment_program_counter()

    def jump_if_zero(self, address: str):
        """Jumps to a specific address if the accumulator is zero."""
        if self.show_steps:
            print(f"Note: Jump to address {str(address).zfill(2)} if the accumulator is zero.")
        if self.processor_repository.processor.accumulator == 0:
            self.processor_repository.processor.program_counter = int(address)
        else:
            self.processor_repository.processor.increment_program_counter()

    def halt(self):
        """Halts the program."""
        if self.show_steps:
            print("Note: Halt the program and display memory state.")
        print("Program halted...")
        print()
        self.processor_repository.memory_controller.display()
        exit()

    def create_store_dto(self, address: str, value: str) -> StoreDataDto:
        """Creates a StoreDataDto with the given address and value."""
        try:
            return StoreDataDto(address=Address(address), data=DataValue(value))
        except MemoryError as e:
            print(f"Failed to create StoreDataDto: {e}...")
            return None 

    def create_read_dto(self, address: str) -> ReadDataDto:
        """Creates a ReadDataDto with the given address."""
        try:
            return ReadDataDto(address=Address(address))
        except MemoryError as e:
            print(f"Failed to create ReadDataDto: {e}...")
            return None  
