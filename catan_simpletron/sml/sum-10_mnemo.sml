LoadI   10
Store   counter -  14    
LoadI   0    
Read    n - 16   
LoadM   obtain - 15      
AddM    n 
Store   obtain    
LoadM    counter    
SubI     1
JZ      end_if_zero - 12  
JMP      jump - 01   
Write    obtain 
Halt    stop   
Variable    00
Variable    00
