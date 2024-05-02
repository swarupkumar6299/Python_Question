#pattern
"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""
for r in range (5,0,-1):
    for c in range (1,6):
        print(r,end=' ')
    print()

print("---------------------------------")
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for r in range (1,6):
    for c in range(1, r+1):
        print(r,end=' ')
    print()
print("--------------------------------")

"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
for r in range(5,0,-1):
    for c in range(1,r+1):
        print(r,end=' ')
    print()

print("-----------------------------")

"""
1 1 1 1 1
2 2 2 2
3 3 3 
4 4
5
"""
for r in range(1,6):
    for c in range(1,7-r):
        print(r,end=' ')
    print()

print("--------------------------------")
"""
5
4 4
3 3 3
2 2 2 2
1 1 1 1
"""
for r in range(5,0,-1):
    for c in range (1,7-r):
        print(r,end=' ')
    print()

print("----------------------------------")
for r in range(1,6):
    for c in range(1,6):
        print(c,end=' ')
    print()
print("----------------------------------")
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
for r in range(5,0,-1):
    for c in range (1,r+1):
        print(c, end=' ')
    print()
print("----------------------------------")
for r in range(1,6):
    for c in range(1,r+1):
        print(r,end=' ')
    print()
print("----------------------------------")
"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
for r in range (1,6):
    for c in range (1,6):
        print(r,end=' ')
    print()