#Pattern 
"""
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
"""
for r in range(1,6):
    for c in range(1,6):
        print(1,end=" ")
    print()
print("---------------------------------")

"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
for r in range (1,6):
    for c in range(1,6):
        print(r,end=' ')
    print()