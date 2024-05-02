# Write a program to generate prime numbers from 2 to 30
for num in range (2,31):
    count = 0
    for i in range (1,num+1):
        if num%i==0:
         count=count+1
    if count==2:
       print(f"The prime number of 2 to 30 is {num}")