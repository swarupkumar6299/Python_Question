#Write a progrm to find input is armstrong or not
num = int(input("Enter any number:- "))
temp = num
s = 0
while num>0:
    r=num%10
    s=s+(r**3)
    num = num//10
if s==temp:
    print("Armstrong")
else:
    print("Not Armstrong")