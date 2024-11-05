Read        n1              ; Read the first integer and store it in n1 (A)
Read        n2              ; Read the second integer and store it in n2 (B)
LoadM       n1              ; Load the value of n1 (A) into the accumulator
AddM        n2              ; Add the value of n2 (B) to the accumulator
Store       sum             ; Store the result in the variable 'sum' (C)
Write       sum             ; Output the value of 'sum' (C) to the screen
Halt        stop            ; Terminate the program execution
