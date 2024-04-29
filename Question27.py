#Write a progrm to count even and odd digits in a given number
num = int(input("Enter any number:- "))
even_count = 0
odd_count = 0
while num >0:
    r=num%10
    if r %2==0:
        even_count = even_count+1
    else:
        odd_count = odd_count+1
    num =  num//10

print(f'Count of even digit {even_count}')
print(f'Count of odd digit {odd_count}')