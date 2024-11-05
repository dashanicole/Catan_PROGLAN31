Read    14 ; Read user input and save it in address 14 (variable n)
LoadI    01 ; Load the constant value 1 into the accumulator
Store    15   ; Save the value from the accumulator into address 15 (variable factorial)
LoadM    14   ; Load the value of variable n into the accumulator
JZ       12   ; If accumulator is 0, jumto the screen
LoadM    15   ; Load the current value of variable factorial into the accumulator
MulM     14   ; Multiply the accumulator value by variable n
Store    15   ; Store the result from the accumulator back to variable factorial
LoadM    14   ; Load the value of variable n into the accumulator
SubI     01   ; Decrease the value in the accumulator by 1
Store    14   ; Update variable n with the new value from the accumulator
JMP      04   ; Jump back to address 04 to repeat the process
Write    15   ; Output the value of variable factorial 
HALT     43   ; Terminate the programp to address 12 (base case for factorial)
Variable 00   ; Initialize variable n
Variable 00   ; Initialize variable factorial