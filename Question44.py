#Write a progran sum of following series (accept values of x and n from user)
n1 = int(input("Enter the value of X:- "))
n2 = int(input("Enter the value of Y:- "))
s=1
for num in range (1,n2+1):
    fact=1
    for i in range (1,num+1):
        fact*=i
    s=s+n1**num/fact    #--------> logic
print(f"sum of series is {s}")