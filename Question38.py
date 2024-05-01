# Write a program to display all numbers which are divisible by 11 and not divisible by 2 between 100and 500
for num in range(100,500-1):
    if num%11==0 and num%2!=0:
        print(num)


