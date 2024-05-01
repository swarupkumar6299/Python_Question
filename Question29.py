#Write a program to reverse number


#Method 1
"""
num = input("Enter any number:- ")
rev_num = num[::-1]              # --------> This method is consider only string not integer value
print(f'original number {num}')
print(f'reverse number {rev_num}')
"""
#Method 2
num = int(input("Enter any number:- "))
rev = 0
while num >0:
    r = num%10
    rev=(rev*10)+r
    num = num//10
print(f'Reverse number is {rev}')