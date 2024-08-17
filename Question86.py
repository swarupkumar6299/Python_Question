#Frozenset

'''Frozen is an immutable set, after creating frozenset changes cannot be done .
frozenset does not mutable methods
1 add()
2 remove()
3 discard()
clear()
update()
difference_update()

In application development forozen is used for representing

1. Immutable set
2. Nested set

How to creat forezen set
forezenset():Creat empty frozenset
frozenset(iterable): Creat frozrnset reading values from iterable'''

fs1= frozenset()
print(fs1,type(fs1))

fs2=frozenset({10,20,30,40,50,60,70})
print(fs2)

f3= frozenset({'p','y','t','h','o','n'})
frozenset("python")
for value in f3:
    print(value)


A = {(frozenset(range(10,60,10)),frozenset(range(60,10,10)))}
print(A)

for s in A:
    print(s)
for s in A:
    for value in s:
        print(value,end='')
    print()
