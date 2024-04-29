#Write a program to find the length of number or count of digit
# Metho 1

num = input("Enter any number:- ")
x=len(num)
print(x) #This method is not for every question

#Metho 2

num = int(input("Enter any number:- "))
c=0
while num>0:
    c=c+1
    num=num//10
    print(f'Count of digit or length of number is {c}')

