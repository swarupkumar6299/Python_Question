#Write a program to find input number is palindrome 
num = int(input("enter any number:- "))
temp = num
rev = 0
while num >0:
    r = num%10
    rev = (rev*10)+r
    num = num//10
if rev == temp:
    print(f'Given number is palindrome {temp}')
else:
    print(f'Given number is not palindrame {temp}')