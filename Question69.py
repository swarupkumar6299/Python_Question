"""
List Comprehension:- Comprehension is another way of creating list.
List comprehension allow creating list by including for loop and if inside squire brackets.
"""
"""
list1=[0]
print(list1)
list2=[0 for i in range(10)]
print(list2)
list3=[n for n in  range(1,21)]
print(list3)
list5 = [int(input())for i in range(5)]
print(list5)
list7=[n**2 for n in range(1,11)]
print(list7)"""
#Write a program to read 3x3 matrix and display
matrix1 = [[int(input())for j in range(3)]for i in range(3)]
print(matrix1)
matrix2=[[int(input())for j in range(3)]for i in range(3)]
print(matrix2) 