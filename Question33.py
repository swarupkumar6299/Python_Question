#Write a program to generate math table for input number
num = int(input("Enter any digit:- "))
for i in range(1,11):
    pr=num*i
    print(f'{num} x {i} = {pr}')