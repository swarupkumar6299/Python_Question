#Write a program to find 2nd maximum value
n = int(input("Enter the value:- "))
list1=[]
for i in range(n):
    value=int(input("Enter any number:- "))  
    list1.append(value)

    list1.sort(reverse=True)
    count=list1.count(max(list1))
print(f'Second Maximum value{list1[count]}')