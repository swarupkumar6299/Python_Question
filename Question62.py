#Write a program to remove duplicate values from list without conversion of set.
list1=[1,2,6,4,5,6,7,8,9,5,6,7,4]
list2=[]
for value in list1:
    if value not in list2:
        list2.append(value)
print(list1)
print(list2)
