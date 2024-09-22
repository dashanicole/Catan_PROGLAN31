'''
    CATAN, Diether D. BSCS 3A
    Simpleton Memory
'''
class Simpletron:
    def __init__(self):
        # Initialize memory (100 locations with +0000)
        self.memory = ['+0000'] * 100

    def display_memory(self):
        # Display the memory in a formatted way
        print("\nMEMORY:")
        print("         " + "\t".join(map(str, range(10))))
        for i in range(0, 100, 10):
            print(f"{i:02d}\t" + "\t".join(self.memory[i:i+10]))

def main():
    # Create an instance of Simpletron
    simpletron = Simpletron()

    # Example Test Program: Checking if a number is even or odd
    simpletron.memory[0] = "+1009"  # READ A
    simpletron.memory[1] = "+2009"  # LOAD A
    simpletron.memory[2] = "+3802"  # MODI 2
    simpletron.memory[3] = "+4208"  # JZ 08 (jump if zero)
    simpletron.memory[4] = "+1109"  # WRITE A (odd)
    simpletron.memory[5] = "+4009"  # JMP 09 (jump to end)
    simpletron.memory[6] = "+1110"  # WRITE 0 (even)
    simpletron.memory[7] = "+4300"  # HALT
    simpletron.memory[9] = "+0000"  # Variable A
    simpletron.memory[10] = "+0001"  # Even number check result

    # Display the memory
    simpletron.display_memory()

if __name__ == "__main__":
    main()
