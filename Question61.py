#Write a program to find nth maximum value
n = int(input("Enter the value:- "))
list1 = []
for i in range (n):
    value=int(input("Enter any value:- "))
    list1.append(value)
m=int(input("Enter nth value:- "))
set = set(list1)
list1 = list(set)
list1.sort(reverse=True)
print(f'nth maximum is {list1[m-1]}')