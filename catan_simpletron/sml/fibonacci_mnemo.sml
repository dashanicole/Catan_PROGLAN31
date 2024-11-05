Read     n            ; Read an integer value and store it in variable n
LoadI    0            ; Load the value 0 into the accumulator (F(0))
Store    fib0         ; Store F(0) in variable 'fib0'
LoadI    1            ; Load the value 1 into the accumulator (F(1))
Store    fib1         ; Store F(1) in variable 'fib1'

LoadM    n            ; Load the value of n into the accumulator
JZ       @end goto _       ; If n is 0, jump to @end (F(0) is already stored)
LoadM    n            ; Load n into the accumulator again
SubI     1            ; Subtract 1 from n (to calculate F(n-1))
Store    n            ; Store n-1 back to n

; Loop to calculate Fibonacci
; @loop
LoadM    fib0 goto @loop       ; Load F(n-2) into the accumulator
AddM     fib1        ; Add F(n-1) to the accumulator
Store    fib_next    ; Store the result as F(n)

; Update variables for the next iteration
LoadM    fib1        ; Load F(n-1) into the accumulator
Store    fib0        ; F(n-2) becomes F(n-1)
LoadM    fib_next    ; Load F(n) into the accumulator
Store    fib1        ; F(n) becomes F(n-1)

; Decrement n
LoadM    n            ; Load n into the accumulator
SubI     1            ; Subtract 1 from n
Store    n            ; Store the decremented value back to n

; Check if we should continue
LoadM    n            ; Load n into the accumulator
JZ       @end        ; if n is zero goto write
JMP      @loop        ; If n is not zero, jump back to loop

Write    fib1 goto @end         ; Output the last computed Fibonacci number (F(n))
Halt     stop         ; Terminate the program execution
