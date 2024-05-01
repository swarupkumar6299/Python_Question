#Write a program to accept a number and check wether it is perfect number or not.
sum=0
num = int(input("Enter any number:- "))

for i in range(1,num):
    if num%i==0:
       sum = sum+i
    else:
        pass
if num == sum:
     print(f" Given number {num} is perfect")
else:
         print(f" Given number {num} is not perfect")   

