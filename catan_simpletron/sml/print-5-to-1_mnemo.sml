LoadI   5               ; Load the immediate value 5 into the accumulator
Store   n goto @a       ; Store the value from the accumulator into variable n and save point @a
JZ      @b goto _       ; If the accumulator is zero, jump to @b (exit point)
Write   n               ; Output the current value of n
SubI    1               ; Subtract 1 from the value in the accumulator (decrement n)
JMP     @a                ; Jump back to label @a (continue the loop)
Halt    @a goto @b      ; Halt the program execution base on the exit point @b