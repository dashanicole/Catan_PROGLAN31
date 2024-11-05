from .processor_operations import ProcessorOperations 
from typing import Callable, Dict

OpcodeMappingType = Dict[str, Callable[[str], None]]

#TODO type check for processor
def operation_mapping(processor) -> OpcodeMappingType:
    operation = ProcessorOperations(processor, show_steps=True)  

    opcode_mapping: OpcodeMappingType = {
        "10": operation.read,
        "11": operation.write,
        "20": operation.load_m,
        "21": operation.store_m,
        "22": operation.load_i,
        "30": operation.add_m,
        "31": operation.sub_m,
        "32": operation.div_m,
        "33": operation.mod_m,
        "34": operation.mul_m,
        "35": operation.add_i,
        "36": operation.sub_i,
        "37": operation.div_i,
        "38": operation.mod_i,
        "39": operation.mul_i,
        "40": operation.jump,
        "41": operation.jump_if_negative,
        "42": operation.jump_if_zero,
        "43": operation.halt,
    }

    return opcode_mapping
