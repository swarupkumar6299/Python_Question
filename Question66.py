"""
Copy of list
python support two types of copies
1. Shallow Copy
2. Deep copy

Shallow copy---> copy() method of list creat shallo copy.
shallow copy is a reference copy. in shallow copy, python creat a new list by copying reference copy, python creat a ner list by copying reference/address of objects found in original list
"""
"""
list1=[10,20,30,40,50]
list2=list1.copy()
print(list2)

list1=[10,20,30,[40,50]]
print(list1[0],list1[1],list1[2],list1[3])
list2=list1.copy()
print(list2)
list1[3].append(60)#------> append mean add any value 
print(list1)
print(list2)
list2[3][0]=99
print(list2)
print(list1)
list1=[10,20,30,40,50]
list2=list1[:]
print(list1)

"""
"""
Deep copy:- Deep copy is object copy. in deep copy python creat new list by copying object found original list
"""
list1=[10,20,30,[40,50]]
import copy
list2=copy.deepcopy(list1)
print(list2)
list1[3].append(99)
print(list1)
print(list2)
list2[3][0]=55
print(list2)
print(list1)
#reverse():- reverse element of the list
list1.reverse()
print(list1)
list1 = [100,200,300]
list2=list1[::-1]
print(list1)
print(list2)
"""
s.pop() or s.pop(i) retrieves the item at i and also remove it form s
List can be used for implementing stack data styructure .
Stack organizes data using LIFO order . LIFO stand for last in first out.
The element/item inserting last is removing first  
"""
list1 = [10,20,30,40,50]
print(list1)
x=list1.pop()
print(x)
print()
print(list1)
y=list1.pop()
print(y)
print(list1)
z=list1.pop(0)
print(z)
print(list1)
