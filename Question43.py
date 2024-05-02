# Write a program to generate factorial for 1 to 10
for num in range(1,11):
    fact=1
    for i in range (1,num+1):
        fact=fact*i
    print(f"The factorial of {i} is {fact}")