# Write a program to print sum of n numbers, input n numbers from keyboard
num = int(input("Enter a digit:- "))
c = 0
for i in range(1,num+1):
    if num%i==0:
        c=c+1
if c==2:
    print(f"{num}it's prime number")
else:
    print(f"{num} is not prime")