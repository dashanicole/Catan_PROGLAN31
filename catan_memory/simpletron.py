from os import system, path

class Simpletron:
    def __init__(self, memory_size=100) -> None:
        self.accumulator = 0  # Holds the current value
        self.programCounter = 0  # Starting point of the program
        self.instructionRegister = 0  # Current instruction to execute
        self.operationCode = 0  # Operation to use
        self.operand = 0  # Memory location to use
        self.memory = ["+0000"] * memory_size
        self.isRunning = True  # False if 43 (Halt)
        self.placer = 0  # To track where to store the next instruction
        # Mapping of SML commands to operation codes
        self.opcode_map = {
            'Read': 10,
            'Write': 11,
            'LoadM': 20,
            'Store': 21,
            'AddM': 30,
            'SubM': 31,
            'DivM': 32,
            'MulM': 33,
            'Branch': 40,
            'BranchZ': 41,
            'BranchN': 42,
            'Halt': 43
        }

    def store_data(self, word: str) -> None:
        self.memory[self.placer] = word
        self.placer += 1  # Increment the placer for every word inserted

    def execute(self) -> None:
        self.isRunning = True
        while self.isRunning:
            word = self.memory[self.programCounter]
            self.instructionRegister = word
            
            # Extract the operation code
            if word in self.opcode_map:
                self.operationCode = self.opcode_map[word]
            else:
                print(f"Error: Invalid instruction '{word}' at memory location {self.programCounter}")
                self.isRunning = False
                continue
            
            # Handle operations
            print(f"\nExecuting {word} (Opcode: {self.operationCode})...")
        
            if self.operationCode == 10:  # Read input
                self.operand = int(input("Enter the memory location to store input: "))
                value = int(input("Enter an integer: "))
                self.memory[self.operand] = self.format_number(value)
            elif self.operationCode == 11:  # Output
                self.operand = int(input("Enter the memory location to read output from: "))
                print(f"Output (Memory[{self.operand}]): {self.memory[self.operand]}")
            elif self.operationCode == 20:  # Load into accumulator
                self.operand = int(input("Enter the memory location to load from: "))
                self.accumulator = int(self.memory[self.operand])
            elif self.operationCode == 21:  # Store from accumulator
                self.operand = int(input("Enter the memory location to store to: "))
                self.memory[self.operand] = self.format_number(self.accumulator)
            elif self.operationCode == 30:  # Add
                self.operand = int(input("Enter the memory location to add from: "))
                self.accumulator += int(self.memory[self.operand])
            elif self.operationCode == 31:  # Subtract
                self.operand = int(input("Enter the memory location to subtract from: "))
                self.accumulator -= int(self.memory[self.operand])
            elif self.operationCode == 32:  # Divide
                self.operand = int(input("Enter the memory location to divide by: "))
                if int(self.memory[self.operand]) == 0:
                    print("Error: Division by zero")
                    self.isRunning = False
                else:
                    self.accumulator //= int(self.memory[self.operand])
            elif self.operationCode == 33:  # Multiply
                self.operand = int(input("Enter the memory location to multiply by: "))
                self.accumulator *= int(self.memory[self.operand])
            elif self.operationCode == 40:  # Branch to address
                self.programCounter = self.operand
                continue  # Skip the programCounter increment for branches
            elif self.operationCode == 41:  # Branch if zero
                if self.accumulator == 0:
                    self.programCounter = self.operand
                    continue  # Skip the programCounter increment for branches
            elif self.operationCode == 42:  # Branch if negative
                if self.accumulator < 0:
                    self.programCounter = self.operand
                    continue  # Skip the programCounter increment for branches
            elif self.operationCode == 43:  # Halt
                self.isRunning = False
            else:  # If there's no valid opcode
                print(f"Error: Invalid opcode {self.operationCode}")
                self.isRunning = False

            self.dump()  # Display memory after each operation
            input("\n\nPress Enter to continue...")  # Wait for user input before next operation

            self.programCounter += 1  # Increment the program counter

    def format_number(self, number) -> str:
        # Formats the number to +0000 style.
        return f"+{abs(int(number)):04d}" if int(number) >= 0 else f"-{abs(int(number)):04d}"

    def dump(self) -> None:
        print(f"Accumulator:          {self.format_number(self.accumulator)}")
        print(f"Program Counter:      {self.programCounter}")
        print(f"Instruction Register: {self.instructionRegister}")
        print(f"Operation Code:       {self.operationCode}")
        print(f"Operand:              {self.operand}")
        print("\nMemory: ")  

        # Print memory
        for x in range(-1, 10):
            print(f"{'' if x == -1 else x % 10:>6}", end="  ")

        size = len(self.memory)
        for k in range(size):
            if k % 10 == 0:
                print(f"\n{'00' if k == 0 else k:>6}", end="  ")
            print(f"{self.memory[k]:>6}", end="  ")

def loader(filename: str) -> list:
    program: list = []
    if path.exists(filename):
        with open(filename) as file:
            for line in file:
                # Strip comments and whitespace from each line
                instruction = line.split('#')[0].strip()
                if instruction:  # Only add non-empty instructions
                    program.append(instruction)
    return program

def main() -> None:
    memory_size = 100
    simpletron = Simpletron(memory_size)

    while True:  # Loop to allow multiple executions
        filename: str = input("\nEnter the filename of the program to run (or 'exit' to quit): ")
        
        if filename.lower() == 'exit':
            print("\nExiting the Simpletron...")
            break  # Exit the loop

        program: list = loader(filename)

        for item in program:
            # Remove any trailing whitespace or comments
            command = item.strip()
            if command:  # Ensure command is not empty
                simpletron.store_data(command)  # Store command as string

        # Show the memory state after loading the instructions
        print("\nMemory state after loading the program:")
        simpletron.dump()  # Display the current memory state
        
        # Prompt to continue
        input("\n\nPress Enter to continue...")  # Wait for user input before executing

        # Execute the program with the loaded instructions
        simpletron.execute()  

        # Ask if the user wants to run another program
        continue_choice = input("\nDo you want to run another program? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("\nExiting the Simpletron...")
            break  # Exit the loop

if __name__ == "__main__":
    main()