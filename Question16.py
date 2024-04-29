#Writ a program to check whether the last digit of a number (enterd by user) is divisibler by 3 or not
num = int(input("Enter your Number:- "))
last_digit = num%10
if last_digit%3==0:
    print(f"Yes!! enter yor number {num} is divisible by 3")
else:
    print(f"no, Enter your number {num} is not divisible by 3")