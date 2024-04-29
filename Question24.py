#Write a program to print alphabets  A to Z as well as a to z.
n = 65
while n <=90:
    print(f'{n} ----> {chr(n)}',end=' ')
    n=n+1
print()
n=97
while n<=122:
    print(f'{n} ------> {chr(n)}',end=' ')
    n=n+1