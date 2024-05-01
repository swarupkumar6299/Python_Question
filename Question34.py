# Write a program to find factorial of input number.
num = int(input("Enter a digit:- "))
fact=1
for num in range(1,num+1):
    fact=fact*num
print(f'Given digit {num} factorial is {fact}')
