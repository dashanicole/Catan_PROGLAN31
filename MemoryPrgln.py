'''
    CATAN, Diether D. BSCS 3A
    Simpleton Memory
'''
# Initialize memory (100 locations with +0000)
memory = ['+0000'] * 100

# Initialize registers
accumulator = '+0000'
programCounter = 0
instructionRegister = '+0000'
operationCode = 0
operand = 0

# Function to display the registers and memory in the requested format
def display_simpletron_state():
    # Display the registers
    print("REGISTERS:")
    print(f"accumulator:\t\t {accumulator}")
    print(f"programCounter:\t\t    {programCounter:02d}")
    print(f"instructionRegister:\t {instructionRegister}")
    print(f"operationCode:\t\t    {operationCode:02d}")
    print(f"operand:\t\t    {operand:02d}")
    
    # Display the memory
    print("\nMEMORY:")
    print("         " + "\t".join(map(str, range(10))))
    for i in range(0, 100, 10):
        print(f"{i:02d}\t" + "\t".join(memory[i:i+10]))

# Main function to execute the program
def main():
    # Call the function to display the state
    display_simpletron_state()

# Ensure the script runs the main function if executed directly
if __name__ == "__main__":
    main()
