#write a progrm to print sum of digits of input number
num = int(input("Enter any number:- "))
s=0
while num>0:
    r=num%10
    s=s+r
    num = num//10 
    print(f'sum of digit {s}')