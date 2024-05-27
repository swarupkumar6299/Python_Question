"""
Nested List:- Creating list inside is called nested list
Represented list as an element  inside list is called nested.
In nested list data is organized logically by dividing into rows and column

list1= [10,20,30,40,50]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
list2=[[10,20],[30,40],[50,60]]
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[2][1])
"""
#Reading element from nested list using index

list1= [[10,20,30],[40,50,60],[70,80,90]]
for i in range(3):
    for j in range(3):
        print(list1[i] [j], end=' ')
print()

#Reading element from nested list without using index
list1= [[10,20,30],[40,50,60],[70,80,90]]
for a in list1:
    for b in a:
        print(b ,end=' ')
    print()
list1= [[10,20,30],[40,50,60],[70,80,90]]
print(list1[-1])
print(list1[-1][-1])
print(list1[-1][0])
print(list1[0][-1])
#Write a program to add matrices
matrix1=[[1,2],[3,4]]
matrix2=[[5,6],[7,8]]
matrix3=[]
for i in range(2):
    row=[]
    for j in range(2):

        row.append(matrix1[i][j]+matrix2[i][j])
    matrix3.append(row)
print(matrix1)
print(matrix2)
print(matrix3)
#Write a program to creat 3x3 matrix and display 
matrix1= []
print("Enter element of matrix:- ")
for i in range(3):
    row =[]
    for j in range(3):
        value=int(input("Enter any value:- "))
        row.append(value)
    matrix1.append(row)
print(matrix1)
#Write a program to read mark of M student and N subject
M = int(input("Enter how many students? "))
N = int(input("Enter how many subjects? "))
mark = []
for i in range(M):
    row=[]
    for j in range(N):
        s = int(input("Enter mark:- "))
        row.append(s)
    mark.append(row)

for i in range(M):
    total = sum(mark[i])
    avg = total/N
    result = "pass"
    for j in range(N):
        if mark[i][j]<40:
            result = "fail"
            break
    print(mark[i],total,avg,result)