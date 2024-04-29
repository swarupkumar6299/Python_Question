#Write a program to input 10 numbers and print Sum ,Average
s = 0
i = 1
while i<=10:
    num = int(input("Enter any number:- "))
    s=s+num
    i=i+1
average = s/10
print(f"sum is {s}")
print(f"Average is {average:.2f}")


