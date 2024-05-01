num1=int(input("Enter any value X:- "))
num2=int(input("Enter any value y:- "))
fact=1
sum=1
for i in range(1,num1+1):
        fact=fact*i
        sum=sum + (num2**i)/fact
print(f"sum of series {sum}")