'''Recursion Function
--> Recursive Function call is nothng but calling function itself.
--> In recursive function call, calling function and called function both are same.
--> Fuction recursion allow repeating same function number of times or until given condition.
Function recursion required 3 statements
1. Initialization statement
2. condition
3  update statement'''

def print_numbers(n):
    if n>1:
        print_numbers(n-1)
    print(n)
    
print_numbers(5)

def display_numbers(n):
    if n<5:
        display_numbers(n+1)
    print(n)

display_numbers(1)
    