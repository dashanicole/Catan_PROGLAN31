00    1014    ; Read user input and save it in address 14 (variable n)
01    2201    ; Load the constant value 1 into the accumulator
02    2115    ; Save the value from the accumulator into address 15 (variable factorial)
03    2014    ; Load the value of variable n into the accumulator
04    4212    ; If accumulator is 0, jumto the screen
13    4300    ; Terminate the programp to address 12 (base case for factorial)
05    2015    ; Load the current value of variable factorial into the accumulator
06    3414    ; Multiply the accumulator value by variable n
07    2115    ; Store the result from the accumulator back to variable factorial
08    2014    ; Load the value of variable n into the accumulator
09    3601    ; Decrease the value in the accumulator by 1
10    2114    ; Update variable n with the new value from the accumulator
11    4004    ; Jump back to address 04 to repeat the process
12    1115    ; Output the value of variable factorial 
14    0000    ; Initialize variable n
15    0000    ; Initialize variable factorial
