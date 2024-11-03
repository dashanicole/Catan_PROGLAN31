
"""
    @credits ChatGpt (wrap_in_border)
"""
def wrap_in_border(dump_output: str, memory_output: str):
    """Wraps the processor dump and memory display in an ASCII border."""
    content = dump_output + "\n" + memory_output
    lines = content.split("\n")
    max_length = max(len(line) for line in lines)
    
    border = "-" * (max_length + 2)
    print(border)
    for line in lines:
        print(f" {line.ljust(max_length)} ")
    print(border)

def print_welcome():
    print("\n----- WELCOME TO SIMPLETRON -----")
    print("Program loaded successfully...\n")


def print_usage():
    print("\nuse:\tsimpletron filename.sml [-s]")
    print()
    print("\t- runs the Simpletron Machine Language Program stored in the file filename.sml")
    print("\t- For more details on the Simpletron Machine Language and how to write Simpletron programs, please refer to the Readme.txt file.")
    print()
    print("option:")
    print("-s:\texecutes the program one instruction at a time and gives the state of the Simpletron after each instruction\n")



