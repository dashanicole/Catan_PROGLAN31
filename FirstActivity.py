'''
CATAN, Diether D. 
Python
3:00-4:30 MW
-------------------------------------------------------------------------
A program that would accept a positive integer value not greater than 20 
that represents the FIRST number of the list and display the pattern given 
similar to the example below

Example:
n(1..20):7
7 6 5 4 3 2 1
6 5 4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

def displayPattern(num):
    try:
        num = int(num)
        while True:
            if num <= 0 or num > 20:
                raise ValueError("Please enter a positive integer between 1 and 20")
            else:
                for x in range(num, 0, -1):
                    for y in range(x, 0, -1):
                        print(y, end=" ")
                    print()
                print("\nThe End.")
                break
            
    except ValueError as ve:
        print(f"Error: {ve}. \nPlease enter a valid integer.")
        num = input("\nEnter a positive integer (1-20): ")
        displayPattern(num)

num = input("Enter a positive integer (1-20): ")
displayPattern(num)

