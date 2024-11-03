00    ReadA    ; Read user input and save it in address 14 (variable n)
01    LoadI   ; Load the constant value 1 into the accumulator
02    Store    ; Save the value from the accumulator into address 15 (variable factorial)
03    LoadM    ; Load the value of variable n into the accumulator
04    JZ       ; If accumulator is 0, jumto the screen
13    HALT     ; Terminate the programp to address 12 (base case for factorial)
05    Store    ; Load the current value of variable factorial into the accumulator
06    MulM       ; Multiply the accumulator value by variable n
07    Store    ; Store the result from the accumulator back to variable factorial
08    LoadM    ; Load the value of variable n into the accumulator
09    SubI     ; Decrease the value in the accumulator by 1
10    Store    ; Update variable n with the new value from the accumulator
11    JMP      ; Jump back to address 04 to repeat the process
12    Write    ; Output the value of variable factorial 
14    VariableA    ; Initialize variable n
15    VariableB    ; Initialize variable factorial