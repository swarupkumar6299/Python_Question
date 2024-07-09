list1=[1,2,3,4,5,6,7,8,9,10]

b=map(lambda a:a**2,list1)
for value in b:
    print(value,end=' ')

print()
c = map(lambda a:a if a%2==0 else None,list1)
for value in c:
    print(value,end=' ')
