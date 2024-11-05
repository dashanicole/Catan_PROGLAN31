Read     n            ; Read an integer value and store it in variable n
LoadI    1            ; Load the value 1 into the accumulator
Store    fact         ; Store the value of the accumulator into variable 'fact'
LoadM    n            ; Load the value of n into the accumulator
JZ       @a goto @b   ; If the accumulator is 0, jump to @a (end of computation), otherwise continue
LoadM    fact         ; Load the current value of 'fact' into the accumulator
MulM     n            ; Multiply the accumulator by the value of n
Store    fact         ; Store the updated value back into 'fact'
LoadM    n            ; Load the current value of n into the accumulator
SubI     1            ; Subtract 1 from the value in the accumulator
Store    n            ; Store the decremented value back into n
JMP      @b           ; Jump back to continue the loop
Write    fact goto @a ; Output the value of 'fact' to the screen, then jump to @a
Halt     stop         ; Terminate the program execution
