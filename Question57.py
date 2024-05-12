#Write a program to print sum elements of the list
list1= list(range(10,110,10))
print(list1)

sum=0
for i in range(len(list1)):
    sum= sum+list1[i]
    print(f'sum is {sum}')