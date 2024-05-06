num=1
for r in range(1,6):
    for c in range(1,6):
        if c<=r:
            print(num,end=' ')
            num=num+1
    print()
print("-------------------------------------------------------------------------")

for r in range(1,6):
    for c in range(1,6):
        if c<=r:
            if c%2==0:
                print("0",end=' ')
            else:
                print("1",end=' ')
    print()
print("---------------------------------------------------------------------------")

for r in range(1,6):
    for c in range(1,6):
        if c<=r:
            if c%2==0:
                print("*",end=' ')
            else:
                print("$",end=' ')
    print()
print("-----------------------------------------------------------------------------")
for r in range(65,70):
    for c in range(65,70):
        if c<=r:
            print(chr(r),end=' ')
        else:
            print(' ',end=' ')
    print()
print("---------------------------------------------------------------")
for r in range(65,70):
    for c in range(65,70):
        if c<=r:
            print(chr(c),end=' ')
        else:
            print(' ',end=' ')
    print()
print("------------------------------------------------------------------------")
for r in range(1,6):
    for c in range(1,6):
        if c==r:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print("---------------------------------------------------------------------------")
for r in range (1,6):
    for c in range(1,6):
        if c==6-r:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

print("-----------------------------------------------------------------------")
for r in range(1,6):
    for c in range(1,6):
        if (c==r) or (c==6-r):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
    