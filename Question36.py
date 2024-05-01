# Write a program to print sum of n numbers, input n numbers from keyboard
s=0
digit = int(input("Enter tho no. of digit sum:- "))
for i in range(digit):
    num= int(input("Enter the number:- "))
    s=s+num
print(f"Given number {num} of sum is {s} :- ")
