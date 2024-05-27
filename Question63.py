#Write a program to count each element in list 
list1=[1,2,6,6,3,6,7,8,4,5,6,7,8,9]
list2=[]
for value in list1:
    if value not in list2:
        list2.append(value)
for value in list2:
    count=list1.count(value)
    print(f'{value}------->{count}')