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

    def store_data(self, word: int) -> None:
        format_word = self.format_number(word)
        self.memory[self.placer] = format_word
        self.placer += 1  # Increment the placer for every word inserted

        if format_word == "+4300":
            self.isRunning = False

    def execute(self) -> None:
        self.isRunning = True
        while self.isRunning:
            word = self.memory[self.programCounter]
            self.instructionRegister = word
            format_word = word.split("+")[1]
            self.operationCode = int(format_word) // 100
            self.operand = int(format_word) % 100
            
            # Execute operations based on the operation code
            if self.operationCode == 10:  # Read input
                try:
                    # No individual input needed here, as batch inputs were collected
                    print(f"Reading value from memory location {self.operand} -> {self.memory[self.operand]}")
                except Exception as err:
                    print(f"Invalid Input: {err}")
                    exit()
            elif self.operationCode == 11:  # Output
                print(self.memory[self.operand])
            elif self.operationCode == 20:  # Load into accumulator
                self.accumulator = int(self.memory[self.operand])  
            elif self.operationCode == 21:  # Store from accumulator
                self.memory[self.operand] = self.format_number(self.accumulator)
            elif self.operationCode == 30:  # Add
                self.accumulator += int(self.memory[self.operand])  
            elif self.operationCode == 31:  # Subtract
                self.accumulator -= int(self.memory[self.operand])  
            elif self.operationCode == 32:  # Divide
                if int(self.memory[self.operand]) == 0:
                    print("Error: Division by zero")
                    self.isRunning = False
                else:
                    self.accumulator //= int(self.memory[self.operand])  
            elif self.operationCode == 33:  # Multiply
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
                print("\nSimpletron is halting...\n")
                self.isRunning = False
            else:  # If there's no valid opcode
                print(f"Error: Invalid opcode {self.operationCode}")
                self.running = False

            self.dump()  # Display memory after each operation
            input("\n\nPress any key to continue...")  # Wait for user input before next operation

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
        print("Memory: ")  

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
            program = file.readlines()
    return program

def batch_input(simpletron: Simpletron) -> None:
    """
    Collect all input values at once from the user and store them in memory.
    """
    print("\nInput all values required by your program. Enter 'done' when finished:")
    while True:
        try:
            value = input("Enter value or 'done' to finish: ")
            if value.lower() == "done":
                break
            # Convert the value into integer and store it in memory
            simpletron.store_data(int(value))
        except ValueError:
            print("Invalid input, please enter a valid integer.")

def main() -> None:
    memory_size = 100
    simpletron = Simpletron(memory_size)

    while True:  # Loop to allow multiple executions
        filename: str = input("\nEnter the filename of the program to run (or 'exit' to quit): ")
        
        if filename.lower() == 'exit':
            print("\nExiting the Simpletron.")
            break  # Exit the loop

        program: list = loader(filename)

        for item in program:
            instruction: list = item.strip().split("\t")
            command = instruction[1]
            simpletron.store_data(int(command))

        # Collect all user inputs in one go before starting execution
        batch_input(simpletron)

        # Now execute the program with the collected inputs
        simpletron.execute()  

        # Ask if the user wants to run another program
        continue_choice = input("\nDo you want to run another program? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("\nExiting the Simpletron.")
            break  # Exit the loop

if __name__ == "__main__":
    main()
