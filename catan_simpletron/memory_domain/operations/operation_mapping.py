from .processor_operations import ProcessorOperations
from typing import Callable, Dict

OpcodeMappingType = Dict[str, Callable[[str], None]]

def operation_mapping(processor) -> OpcodeMappingType:
    operation = ProcessorOperations(processor)  

    # Mapping symbolic opcodes for readability
    opcode_mapping: OpcodeMappingType = {
        "ReadA": operation.read,              # Read input to address
        "Write": operation.write,             # Write output
        "LoadI": operation.load_i,            # Load immediate
        "Store": operation.store_m,           # Store to memory
        "LoadM": operation.load_m,            # Load from memory
        "MulM": operation.mul_m,              # Multiply from memory
        "SubI": operation.sub_i,              # Subtract immediate
        "JMP": operation.jump,                # Unconditional jump
        "JZ": operation.jump_if_zero,         # Jump if zero
        "HALT": operation.halt                # Stop execution
    }

    # Additional numeric mappings for universal access
    opcode_mapping.update({
        "10": operation.read,
        "11": operation.write,
        "20": operation.load_i,
        "21": operation.store_m,
        "22": operation.load_m,
        "34": operation.mul_m,
        "36": operation.sub_i,
        "40": operation.jump,
        "42": operation.jump_if_zero,
        "43": operation.halt
    })

    return opcode_mapping