print("In given list value count +ve,-ve,and zero")
list1=[5,8,9,1,-3,-6,10,-5,-9,-3,0,1,0,4,0,7,-7,9,-12]
pc,nc,zc= 0,0,0

for i in range(len(list1)):
    if list1[i]>0:
        pc+=1
    elif list1[i]<0:
        nc+=1
    else:
        zc+=1
print(f'List is {list1}')
print(f'+ve Count is {pc}')
print(f'-ve Count is {nc}')
print(f'zero Count is {zc}')