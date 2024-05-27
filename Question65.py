#Given a list of numbers, write a Python program to remove multiple elements from a list based on the given condition.

list1 = [12,15,3,10]
list2 = []
print("Before Deleting list is {list1}")
for value in list1:
    if value%3==0:
        list2.append(value)
    elif value%5==0:
        list
print("============================================================")
list1=[10,20,30,40,50]
print(list1)
list1.clear()
print(list1)
print("====================================================================")
list1 = list(range(10,60,10))
print(list1)
list1.insert(0,99)
print(list1)
list1.insert(-2,88)
print(list1)

#slicing operation: slicing is used for inserting more than one value.
#syntax: list-name[start-index:stop-index]=iterable
#Start-index and stop-index must be same
list3 = list(range(10,110,10))
print(list3)
list3[0:0]=[11,12,13]
print(list3)
list3[5:5]=[1,2,3]
print(list3)
