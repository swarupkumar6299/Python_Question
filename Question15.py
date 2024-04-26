#Write a program to display the last digit of a number 
#(hint any number % 10 will return the last digit)
num = int(input("Enter your number:- "))
last_num = num%10
print(f"Last digit of number {num} is {last_num}")