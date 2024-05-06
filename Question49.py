print("================================Pyramid=======================")
space=4
for r in range(1,6):
    for s in range(space):
            print(" ",end=' ')
    for c in range(1,r+1):
          print("* ",end=' ')
    space=space-1
    print()
print("-------------------------------------------------------------------")
space=0
for r in range(5,0,-1):
    for s in range(space):
        print(" ",end=' ')
    for c in range(1,r+1):
         print("* ",end=' ')
    print()
    space=space+1
print("-----------------------------------------------------------------------")

         
    